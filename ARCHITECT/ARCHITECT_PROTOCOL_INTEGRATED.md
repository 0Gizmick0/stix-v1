---
article: VI
name: ARCHITECT — Strategic Problem Decomposition
perspective: CS Bachelor + Software Developer + Computer Engineer
governing_value: JUDGMENT
rule_range: A1–A20
rule_count: 20
---

# ARTICLE VI — ARCHITECT (Integrated Perspective)

---

## A1 — CONCEPT ISOLATION (Formal + Practical + Resource)

**CS (Theory):** Extract the abstract concept — reduce problem to its information-theoretic core. What is the minimal state machine?

**Dev (Real):** Can you describe it in one sentence without jargon? If you can't, you don't understand it.

**Engineer (System):** What hardware/system components does this touch? CPU? I/O? Network? RAM?

**Pattern:**
```
Input: "Build a hotkey daemon for voice-to-text"

CS decompose: 
  State machine: [listening] → [hotkey detected] → [recording] → [silence detected] → [transcribing] → [clipboard written]
  Minimal states: 6
  Complexity: O(n) where n = seconds of audio
  
Dev reality:
  One sentence: "Capture Ctrl+Alt+W, record until silence, transcribe, copy to clipboard"
  Edge cases: What if already recording? What if clipboard fails? What if microphone unplugged mid-recording?
  
Engineer constraints:
  CPU: Need real-time audio processing (requires low-latency threading)
  I/O: Direct microphone access (needs ALSA/PulseAudio/Wayland interaction)
  RAM: Whisper model in memory (~1GB for 'base' model)
  Permissions: Audio device, clipboard access
```

**Fail mode:** Vague concept that doesn't map to system components.

---

## A2 — SCOPE BOUNDARY (Formal + Practical + Resource)

**CS (Theory):** Define the problem domain mathematically. What are the input set and output set?

**Dev (Real):** Write it as acceptance tests BEFORE coding.

**Engineer (System):** What I/O operations are involved? What can saturate?

**Pattern:**
```
CS formal:
  Input set: {keyboard events} ∩ {Ctrl+Alt+W}
  Output set: {clipboard contents}
  Processing: audio_stream → transcription_model → text
  Boundary: No GUI, no config, no multi-key, no cloud APIs
  
Dev acceptance tests (before code):
  ✅ Ctrl+Alt+W is detected within 100ms of press
  ✅ Recording starts immediately
  ✅ Records for minimum 0.5s, stops at 1.5s silence
  ✅ Transcription completes within 30s
  ✅ Text copied to clipboard
  ✅ No transcription if recording < 0.5s (noise filter)
  ❌ Out of scope: Settings dialog, hotkey remapping, cloud upload
  
Engineer I/O:
  IN: Keyboard events (X11 root window), microphone stream
  OUT: Clipboard data
  Saturation points: Microphone (max sample rate 48kHz), Whisper (model load time), clipboard (usually instant)
```

---

## A3 — CONSTRAINT EXTRACTION (Formal + Practical + Resource)

**CS (Theory):** Formalize constraints as inequalities.

**Dev (Real):** Measure them on your actual system. Don't assume.

**Engineer (System):** Map to actual hardware limits.

**Pattern:**
```
CS formal:
  Time: t_session ≤ 8 hours
  Tokens: T ≤ 8,000
  Files: N ≤ 100KB total input
  
Dev measured:
  $ time python3 -c "import whisper; whisper.load_model('base')" 
  real 45.2s (first run, model download)
  real 2.1s (cached)
  
  $ du -sh ~/.cache/whisper/
  1.4GB (base model)
  
Engineer system:
  CPU: 4 cores available (check: nproc)
  RAM: 4GB total, ~2GB free (check: free -h)
  GPU: None (nvidia-smi returns "command not found")
  Microphone: /dev/snd/pcmC* exists and readable
  X11: DISPLAY=:0, X11_SOCKET=/tmp/.X11-unix/X0
  Wayland: WAYLAND_DISPLAY not set (X11 only)
```

**If any constraint violated, deadlock. Example: Need GPU but none exists → declare infeasible.**

---

## A4 — CRITICAL PATH QUESTION (Formal + Practical + Resource)

**CS (Theory):** What is the bottleneck in the dependency graph?

**Dev (Real):** What breaks first in production?

**Engineer (System):** What resource can't be recovered if it fails?

**Pattern:**
```
CS dependency graph:
  Hotkey detection → Recording → Transcription → Clipboard
  
  Critical path = longest path through DAG
  If hotkey fails: no recording, no transcription
  If recording fails: no transcription, no output
  If transcription fails: no output (but recording still happened, can retry)
  If clipboard fails: data in memory, user can paste manually, not fatal
  
  → Critical path = hotkey + recording (if either fails, entire project fails)
  
Dev production failure:
  "Ctrl+Alt+W never triggers" = most common complaint
  Root causes: pynput incompatible, X11 event not captured, permission denied
  
Engineer system resource:
  Hotkey detection = blocking call on X11 record context
  If this call blocks indefinitely = daemon hangs, CPU at 100%, must kill -9
  If it fails silently = user keeps pressing hotkey, nothing happens, daemon seems broken
  
CRITICAL QUESTION: "Does pynput Listener actually work on Linux X11?"
Answer NO? = Dead end, stop. Don't build rest of system.
```

---

## A5 — DEPENDENCY QUESTIONS (Formal + Practical + Resource)

**CS (Theory):** For each dependency, what is its interface contract? Does it guarantee termination?

**Dev (Real):** Does it have a working PyPI wheel for my platform? Any open issues?

**Engineer (System):** What system resources does it lock?

**Pattern:**
```
Dependency: pynput

CS interface:
  from pynput import keyboard
  listener = keyboard.Listener(on_press=callback)
  listener.start()  # spawns thread
  listener.join()   # blocks until listener stops
  
  Contract: Listener guarantees on_press() called for each KeyPress? 
  Check: Source code → yes, documented
  Termination: Does listener thread exit cleanly?
  Check: Look for daemon=True/False flag
  
Dev reality:
  PyPI: pynput-1.8.1 exists for py3
  Wheel: pyaudio-0.2.14-cp312-cp312-linux_x86_64.whl exists
  Issues: GitHub search "pynput X11 Listener.pressed" → 47 issues, "listener doesn't have pressed" in 3
  Test: Can I import? pip list | grep pynput
  
Engineer system:
  Thread spawned: Need to account in ps aux (2+ processes)
  File descriptors: /dev/input/* access required (check: ls -la /dev/input/)
  Permissions: Must run as user, not root (security)
  Signals: Must handle SIGINT cleanly (Ctrl+C stops daemon)
```

**Resolution:** If answer is NO for any of these, dependency is unsuitable.

---

## A6 — ARCHITECTURE QUESTIONS (Formal + Practical + Resource)

**CS (Theory):** Draw the dependency graph. What are the critical edges? What's the longest path?

**Dev (Real):** How do you test each layer in isolation?

**Engineer (System):** What process/thread model? Where's the I/O bottleneck?

**Pattern:**
```
CS DAG:
  X11Event → Hotkey → Record → Buffer → Transcribe → Parse → Clipboard
  
  Critical path length = 7 edges
  If any edge fails, system fails
  Longest latency edge = Transcribe (30+ seconds for 60s audio)
  
Dev isolation tests:
  Layer 1: "Can we detect Ctrl+Alt+W in isolation?" (test_hotkey.py, no daemon)
  Layer 2: "Can we record 5s of audio to file?" (test_record.py, no hotkey)
  Layer 3: "Can we transcribe a sample audio file?" (test_transcribe.py, no recording)
  Layer 4: "Can we write to clipboard?" (test_clipboard.py, no transcription)
  
Engineer threading:
  Main thread: Block on X11 event listener
  Worker thread 1: Handle recording (spawned on hotkey)
  Worker thread 2: Handle transcription (spawned after recording)
  Issue: Do threads share state safely? Use locks? Queues?
  Answer: Spawn worker, wait for completion, main thread blocked during recording
  Problem: If transcription hangs, main thread stuck, hotkey unresponsive
  Solution: Spawn transcription in daemon thread, don't block main
```

---

## A7 — JARGON EXTRACTION (Formal + Practical + Resource)

**CS (Theory):** Replace English with formal notation. Makes ambiguity visible.

**Dev (Real):** Write pseudocode that matches actual implementation.

**Engineer (System):** Use actual system calls.

**Pattern:**
```
Vague: "Listen for hotkey globally"
Formal: global_hotkey_detected(key_code=18, modifiers={CTRL, ALT})  // 18 = W keycode

Vague: "Record audio"
Formal: audio_stream = pyaudio.open(...); chunk = audio_stream.read(1024); frames.append(chunk)

Vague: "Copy to clipboard"
Formal: pyperclip.copy(transcript_string)  // utf-8 plaintext, max 65KB typical clipboard

Vague: "Stop on silence"
Formal: 
  silence_detected = mean(abs(audio_chunk)) < threshold=0.02
  if silence_detected: consecutive_silence_frames += 1
  if consecutive_silence_frames > max_silence_frames(duration=1.5s): stop_recording()

Engineer system calls:
  X11: XRecord, XQueryKeymap, XGetKeyboardMapping (Xlib)
  Audio: ALSA snd_* calls, or PyAudio wrapper (PortAudio)
  Clipboard: XSel (X11), or xclip, or pyperclip (which uses system commands)
```

**Fail mode:** Vague language masks edge cases. Example: "record audio" doesn't specify sample rate, bit depth, channels.

---

## A8 — SUCCESS CRITERIA LANGUAGE (Formal + Practical + Resource)

**CS (Theory):** Define success as a set of boolean predicates. All must be true.

**Dev (Real):** Write automated tests that verify each predicate.

**Engineer (System):** Measure performance on actual hardware.

**Pattern:**
```
CS predicates:
  P1: ∀ hotkey_press ∈ past_10_presses, hotkey_detected(hotkey_press) = TRUE
  P2: latency(hotkey_press → recording_start) ≤ 100ms
  P3: ∀ audio_chunk ∈ recording, |length(audio_chunk) - expected_length| ≤ 5%
  P4: transcription_result ∈ Valid_UTF8
  P5: clipboard_content = transcription_result (byte-for-byte match)
  
  SUCCESS = P1 AND P2 AND P3 AND P4 AND P5
  
Dev test code:
  def test_hotkey_detection():
    for i in range(10):
      simulate_hotkey_press(Ctrl+Alt+W)
      assert hotkey_detected_event_fired, f"Hotkey {i+1} missed"
  
  def test_latency():
    t0 = time.time()
    simulate_hotkey_press(Ctrl+Alt+W)
    assert recording_started.wait(timeout=0.1), "Recording didn't start within 100ms"
  
  def test_transcription_correctness():
    test_audio = load("test_audio.wav")  # known content
    result = whisper.transcribe(test_audio)
    assert edit_distance(result, expected_text) ≤ 2, "Too many transcription errors"
  
Engineer measured:
  Measure on actual system: benchmark the three slowest operations:
  - Model load: 2.1s (cached)
  - Transcription: 15s for 60s audio (4x realtime on 4-core CPU)
  - Latency: measure with hardware timer if possible, or best-effort
```

---

## A9 — FAILURE MODE LANGUAGE (Formal + Practical + Resource)

**CS (Theory):** Enumerate all possible failure states. What's the failure probability per state?

**Dev (Real):** Have you seen this failure in production? What does it look like in logs?

**Engineer (System):** Which resource exhaustion causes this?

**Pattern:**
```
Failure mode 1: Hotkey not detected

CS state: X11Event received, but Listener.on_press() not called
Probability: P(X11 event generation) ≥ 99%, P(on_press call) ≤ 80% for pynput
Root causes: 
  - Listener not started (code bug)
  - X11 not running (env issue)
  - Listener thread crashed (unhandled exception)
  
Dev logging:
  logger.info("Listener started, entering event loop")
  [silence for 30 minutes]
  → Listener crashed without exception handler
  → add try/except in on_press, log all exceptions
  
Engineer resource:
  File descriptors: /dev/input/* open?
  Permissions: Can user read /dev/input/event*?
  X11 socket: /tmp/.X11-unix/X0 accessible?
  
Failure mode 2: Audio not recorded

CS state: pyaudio.read() returns silence (all zeros)
Root causes:
  - Microphone not detected
  - Permission denied on /dev/snd/
  - Sample rate mismatch
  - Audio device in use by another process
  
Dev check:
  arecord -l  # list audio devices
  pactl list sources  # list PulseAudio sources
  $ timeout 2 arecord test.wav  # Can we record?
  
Engineer resource:
  /dev/snd/pcm* permissions: who can access?
  PulseAudio running? ps aux | grep pulse
  ALSA configuration: /etc/asound.conf or ~/.asoundrc
  
Failure mode 3: Transcription hangs

CS state: whisper.transcribe() blocks indefinitely
Root causes:
  - Model too large for available RAM → swap thrashing
  - GPU mode activated but no GPU → hangs waiting for CUDA
  - File descriptor leak, no resources left
  
Dev timeout:
  result = timeout_call(whisper.transcribe, timeout_seconds=45)
  if timeout: log error, return empty string
  
Engineer resource:
  RAM usage: monitor with watch 'free -h'
  Swap usage: monitor swap if it exists
  GPU: nvidia-smi shows CUDA available?
  Model size: base=1.4GB, small=2.7GB, medium=5.1GB
  → If available RAM < model size, will swap and be very slow
```

---

## A10 — PROOF-OF-CONCEPT SCOPE (Formal + Practical + Resource)

**CS (Theory):** Identify the minimal reproducible case. Can you solve it in a smaller problem space?

**Dev (Real):** Write a 50-line script that answers the critical question.

**Engineer (System):** Does the POC use the same system resources as the full system?

**Pattern:**
```
Critical question: "Does pynput Listener work for global hotkey on Linux X11?"

CS minimal case:
  Input: Keyboard event (Ctrl+Alt+W)
  Output: Boolean (detected or not)
  Test case size: 1 hotkey, 10 presses
  
Dev POC (test_pynput_poc.py):
  from pynput import keyboard
  import time
  
  detected = []
  def on_press(key):
      try:
          if key == keyboard.Key.ctrl_l or key == keyboard.Key.alt_l or chr(key.char) == 'w':
              detected.append(key)
      except: pass
  
  listener = keyboard.Listener(on_press=on_press)
  listener.start()
  print("Listener started. Press Ctrl+Alt+W 10 times...")
  time.sleep(30)
  listener.stop()
  print(f"Detected {len(detected)} keys")
  
Engineer resource check:
  Before running POC:
    free -h                    # Check RAM
    ps aux | grep python       # Check if processes already running
    ls -la /dev/input/         # Check permissions
  After running POC:
    Did it use significant CPU?
    Did any /dev/input/event* get locked?
    Did it handle Ctrl+C cleanly?
```

**Cost: 200 tokens, 15 minutes. If YES → proceed. If NO → dead end, stop.**

---

## A11 — LIBRARY SUITABILITY MATRIX (Formal + Practical + Resource)

**CS (Theory):** For each library, define the interface contract. Does it satisfy your requirements?

**Dev (Real):** Check GitHub issues, PyPI stats, last commit date. Is it maintained?

**Engineer (System):** Does it conflict with other libraries? Does it require elevated privileges?

**Pattern:**
```
Library: pynput

CS interface contract:
  Requirement: Detect keyboard hotkey (Ctrl+Alt+W) without focus
  Interface: Listener(on_press=callback)
  Promise: "Calls on_press() for each global keypress"
  Reality: Does NOT promise global on Wayland. X11 only.
  
Dev repository health:
  GitHub: anthropic-ai/pynput (exists)
  Last commit: 6 months ago (maintained? Maybe)
  Open issues: 200+ (high count = possibly unmaintained)
  Issue "Listener has no .pressed" : CLOSED, "use on_press callback instead"
  
Engineer conflicts:
  Requires: Xlib (python-xlib)
  Conflicts: If you use Wayland, won't work
  Requires: /dev/input/* access (might need group membership)
  Test: $ python3 -c "from pynput import keyboard; print('OK')"
  
Suitability matrix:
  | Criterion | Yes/No | Weight | Score |
  |-----------|--------|--------|-------|
  | Works on Linux X11 | YES | 40% | 40 |
  | Global hotkey support | NO | 40% | 0 |
  | Maintained | MAYBE | 10% | 5 |
  | No elevated privileges | YES | 10% | 10 |
  | TOTAL SCORE | | | 55/100 |
  
  → Score 55 = MARGINAL. Try alternatives before committing.
```

---

## A12 — ALTERNATIVE PATHS (Formal + Practical + Resource)

**CS (Theory):** For each critical decision, what are all feasible algorithms/approaches?

**Dev (Real):** Quick experiment (1 hour max) on each path. Score them.

**Engineer (System):** Which path has lowest resource cost?

**Pattern:**
```
Critical decision: "How to capture global hotkey on Linux?"

Path 1: pynput Listener
  CS: Event-driven callback model
  Dev: 1 hour POC → NO (no .pressed, callback model doesn't help)
  Engineer: Spawns thread, needs X11 socket, moderate CPU
  Score: 55/100 (marginal)

Path 2: X11 XRecord directly (python-xlib)
  CS: Low-level X11 record context, more control
  Dev: 1 hour POC → 
    from Xlib.ext import record
    ctx = record.create_context(...)
    Testing: Does it work? Partially (complex API)
  Engineer: Direct X11 call, needs X server, high CPU (polling)
  Score: 70/100 (viable)

Path 3: evdev (raw input device)
  CS: Direct kernel event capture, lowest level
  Dev: 1 hour POC → 
    from evdev import InputDevice, categorize
    device = InputDevice('/dev/input/event0')
    Testing: Works but needs device enumeration
  Engineer: Direct /dev/input access, requires group membership or sudo, lowest CPU
  Score: 65/100 (viable but permission issues)

Path 4: DBus (via system D-Bus)
  CS: System service model, highest abstraction
  Dev: Check if any service exposes hotkey API
  Testing: No standard hotkey service on Linux
  Score: 20/100 (not viable)

Decision: "Try Path 2 (X11 XRecord) for 1 hour. If it works, deploy it. If not, try Path 3."
```

**Time envelope: 1 hour × 3 paths = 3 hours max before declaring "infeasible" or "choose best viable."**

---

## A13 — PHASE TOKEN BUDGET (Formal + Practical + Resource)

**CS (Theory):** Estimate work as a function of problem size. Use past projects as calibration.

**Dev (Real):** Track actual tokens by phase. Compare to estimate. Adjust.

**Engineer (System):** Account for model load time, API latency, POC overhead.

**Pattern:**
```
CS estimation function:
  tokens_per_phase = base_tokens + (complexity_factor × problem_size) + (unknown_factor × 0.1)
  
  base_tokens = 500 (fixed overhead)
  complexity_factor = 0.5 (tokens per line of code, roughly)
  problem_size = 200 lines (estimated LOC)
  unknown_factor = 20% (buffer for unknowns)
  
  Phase 1 (research POCs): 500 + (0.5 × 100) + 100 = 1,100 tokens
  Phase 2 (design, alternatives): 500 + (0.5 × 50) + 75 = 850 tokens
  Phase 3 (implementation): 500 + (0.5 × 200) + 150 = 1,700 tokens
  Phase 4 (test, debug): 500 + (0.5 × 150) + 100 = 1,050 tokens
  
  BUDGET: 4,700 tokens (~$2.35)
  
Dev actual (whisper daemon):
  Phase 1 (pynput POC): 2,000 tokens (over by 800)
  Phase 2 (X11 alternative): 3,000 tokens (over by 2,150 — dead end, should have stopped)
  Phase 3 (discussions): 2,000 tokens (never started implementation)
  ACTUAL: 7,000 tokens (~$3.50)
  
  Lesson: pynput POC cost more than estimated (wrong POC design?), and we didn't stop at dead end
  
Engineer timing overlay:
  Whisper model load: 45s first run, 2s cached
  POC overhead: "import whisper" alone = 2s (slow import)
  Decision: Run POC without loading full model, only test pynput
  Actual: We loaded whisper during X11 POC (wasted 45s, 500 tokens on irrelevant work)
```

**Budget for whisper daemon should be:**
```
Phase 1 (POC, NO model loading): 500 tokens
Phase 2 (design alternatives): 400 tokens
Phase 3 (implement best path): 1,200 tokens
TOTAL: 2,100 tokens ($1.05)

ACTUAL: 7,000 tokens
WASTE: 4,900 tokens due to wrong POC design + not stopping at dead end
```

---

## A14 — DEAD END DETECTION BUDGET (Formal + Practical + Resource)

**CS (Theory):** What is the minimum cost to prove a path is infeasible?

**Dev (Real):** Name the ONE test that would kill the project. Budget for it upfront.

**Engineer (System):** What's the fastest way to test this on hardware?

**Pattern:**
```
Whisper daemon critical test: "Does pynput Listener support global hotkey on X11?"

CS minimal proof:
  ∃ X ∈ KeyEvent, X = Ctrl+Alt+W, where on_press(X) is called
  Negation: ¬∃ X ∈ KeyEvent such that Listener.on_press() ever calls on_press(Ctrl+Alt+W)
  Cost to prove false: Must run for 30 seconds without ever seeing the event
  
Dev test code:
  def test_pynput_global_hotkey():
    from pynput import keyboard
    detected = False
    def on_press(key):
        nonlocal detected
        detected = True
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    simulate_hotkey(Ctrl+Alt+W)  # hardware simulation or manual press
    time.sleep(2)
    listener.stop()
    return detected  # True or False
  
Engineer timing:
  Test execution: 3 seconds max
  Token cost: 200 tokens (explain test + run + results)
  If FALSE → Stop, declare dead end
  If TRUE → Proceed to next gate
  
Decision gate: 
  "If dead end detected, cost = 200 tokens (acceptable)
   If we ignore dead end and continue: cost = 4,000 tokens (unacceptable)
   Ratio: 1 token to detect vs 20 tokens to waste
   → Always run dead end detection first"
```

---

## A15 — CHECKPOINT COMPRESSION COST (Formal + Practical + Resource)

**CS (Theory):** Checkpointing reduces context size from O(n) to O(log n) where n = messages. How much is saved?

**Dev (Real):** Have you actually measured E25 savings on a real project?

**Engineer (System):** Checkpoint file I/O cost vs token savings.

**Pattern:**
```
CS complexity analysis:
  Without checkpoints: context_size grows linearly with messages
  c(n) = 5KB + (0.5KB × n messages)
  
  With checkpoints every 20 messages:
  c(n) = 2KB checkpoint + (0.5KB × n messages in current phase)
  
  20-message project:
  Without: 5KB + (0.5 × 20) = 15KB context
  With: 2KB + (0.5 × 5) = 4.5KB context
  Savings: 70% (consistent with E25 claim of 60-70%)
  
Dev measured (this session):
  Messages so far: ~60
  Without checkpoint: Estimated 35KB context by message 60
  With checkpoint at message 20: 4KB + new messages
  Actual: We didn't implement E25 fully, but theory checks out
  
Engineer file I/O:
  Writing checkpoint: 2KB file → negligible I/O cost
  Reading checkpoint: 2KB file, no API call needed → negligible latency
  Storage: FORGE_DB/projects/*/phase-N-checkpoint.md → ~500MB for 10K projects (acceptable)
  
Overhead analysis:
  E25 overhead: 10 seconds to write checkpoint (negligible)
  E25 savings: 8,000 tokens per 4-phase project
  Cost/benefit: 1 minute overhead, save $4
  ROI: Only worthwhile for projects ≥ 20 messages or ≥ 2 phases
```

---

## A16 — TWO-ITERATION THRESHOLD (Formal + Practical + Resource)

**CS (Theory):** Two failed iterations on same path = proof the path doesn't work (by induction).

**Dev (Real):** After iteration 2 fails, pivot or stop. Don't iterate 3, 4, 5 times.

**Engineer (System):** Each iteration costs exponentially more as you go deeper (more code, more state).

**Pattern:**
```
Whisper daemon iterations:

Iteration 1: pynput Listener
  Approach: Use pynput.keyboard.Listener for global hotkey
  Time: 2 hours (reading docs, writing code, testing)
  Cost: 5,000 tokens
  Result: FAIL (Listener has no .pressed attribute, can't detect global hotkeys as designed)
  
Iteration 2: X11 XRecord
  Approach: Use python-xlib's record context directly
  Time: 1.5 hours (reading X11 docs, converting pynput code to X11 calls)
  Cost: 3,000 tokens
  Result: FAIL (keysym import path wrong, Listener.pressed still referenced)
  
At this point: E17 should trigger
  ✅ Two iterations complete
  ✅ Both failed on same root cause: "how to capture global hotkey on Linux"
  ✅ Decision: Path doesn't work, stop
  ❌ What we did: Started planning Iteration 3 (evdev) and more
  
CS induction:
  Claim: "This problem (global hotkey on Linux) has no solution with current approach"
  Proof by contradiction: If solution existed, one of 2 iterations would have found it
  Conclusion: Path is infeasible. Stop.
  
Iteration cost escalation:
  Iteration 1: 2 hours, 5KB code, 5,000 tokens
  Iteration 2: 1.5 hours, 4KB code (previous code modified), 3,000 tokens
  Iteration 3 would: 1.5 hours, ??? KB code, 3,000+ tokens (compounding)
  Iteration 4 would: 2 hours, ??? KB code, 4,000+ tokens (more complex, more tokens)
  
  Total wasted tokens if we iterate 3-5 times: 5K + 3K + 3K + 4K = 15,000 tokens
  Actual (stopped after 2): 8,000 tokens
  Saved by E17: 7,000 tokens ($3.50)
```

**Gate: If iteration 2 fails, declare dead end and stop. Always.**

---

## A17 — ASSUMPTION RISK RANKING (Formal + Practical + Resource)

**CS (Theory):** Model assumptions as Boolean predicates. Rank by consequence (impact).

**Dev (Real):** Which assumption, if wrong, breaks everything?

**Engineer (System):** Which assumption is cheapest to test on actual hardware?

**Pattern:**
```
Whisper daemon assumptions ranked:

| Assumption | Consequence | Impact | Test cost | Status |
|------------|-------------|--------|-----------|--------|
| pynput works on Linux | Entire project fails if false | CRITICAL | 200 tokens | ❌ FALSE (tested, failed) |
| X11 is available | Global hotkey doesn't work on Wayland | HIGH | 100 tokens | ✅ TRUE (DISPLAY=:0) |
| Microphone accessible | Recording doesn't work | HIGH | 200 tokens | ✅ TRUE (/dev/snd/ readable) |
| Whisper model fits in RAM | Transcription hangs or crashes | HIGH | 300 tokens | ✅ TRUE (1.4GB < 4GB RAM) |
| Clipboard library works | Output fails silently | MEDIUM | 100 tokens | ✅ TRUE (pyperclip installed) |
| GPU available (optional) | Transcription slower but works | LOW | 50 tokens | FALSE (no GPU) |

CS risk matrix:
  For each CRITICAL/HIGH assumption, compute: P(wrong) × impact
  pynput works: P(0.3) × 100 = 30 (high risk)
  X11 available: P(0.05) × 80 = 4 (low risk, almost certain)
  Microphone: P(0.2) × 80 = 16 (medium risk)
  
  → Rank by risk: pynput (30) > microphone (16) > X11 (4)
  → Test pynput FIRST, microphone second, X11 third
  
Dev test:
  Total test cost to validate top 3 assumptions: 200 + 200 + 100 = 500 tokens
  Value: Eliminates 70% of risk before building
  
Engineer hardware test order:
  1. X11 available: echo $DISPLAY (instant)
  2. Microphone available: ls -la /dev/snd/pcm* (instant)
  3. pynput import: python3 -c "from pynput import keyboard" (2s)
  4. pynput hotkey: run POC (5s)
  
  Total time: 10 seconds on actual hardware
```

**Mandatory:** Test all CRITICAL/HIGH assumptions before APEX work begins.

---

## A18 — ESCAPE HATCH CRITERIA (Formal + Practical + Resource)

**CS (Theory):** Define a termination condition. When do you stop?

**Dev (Real):** "If [specific observable fact], then stop."

**Engineer (System):** What metric tells you it's time to stop?

**Pattern:**
```
Whisper daemon escape hatches:

Hatch 1: POC hotkey detection
  Condition: "If pynput POC doesn't detect Ctrl+Alt+W after 30 seconds of trying"
  Action: STOP, declare dead end
  Cost if triggered: 200 tokens (acceptable, caught early)
  
Hatch 2: Two failed implementations
  Condition: "If two different hotkey libraries both fail"
  Action: Reassess project, consider different approach (not hotkey) or stop
  Cost if triggered: 6,000 tokens (acceptable, E17 rule)
  
Hatch 3: Token budget exceeded
  Condition: "If actual tokens spent > 1.5x budget after phase 2"
  Action: STOP, don't proceed to phase 3
  Budget: 2,100 tokens, 1.5x = 3,150 tokens
  Condition triggered: "After POC + design phases, spent 5,000 tokens"
  Decision: STOP here (but we didn't, we continued)
  
Hatch 4: Model load > budget
  Condition: "If Whisper model load (first run) + POC > 50% of session budget"
  Action: Use smaller model ('tiny') or pre-cache model before session
  
Engineer resource hatch:
  Condition: "If RAM usage exceeds 80% at any point"
  Action: Reduce model size or increase swap, or STOP
  
Decision gate:
  "If any escape hatch is triggered, STOP immediately.
   Do not pivot, do not continue, do not hope for better results.
   STOP is not failure. STOP is wisdom."
```

---

## A19 — DEFINITION OF DONE (Formal + Practical + Resource)

**CS (Theory):** Success is a conjunction of boolean predicates. All must be true.

**Dev (Real):** Write test code that verifies each predicate automatically.

**Engineer (System):** Measure performance: latency, CPU, RAM, I/O.

**Pattern:**
```
Whisper daemon definition of done:

CS formal:
  DONE = P1 ∧ P2 ∧ P3 ∧ P4 ∧ P5 ∧ P6 ∧ P7
  
  P1: Hotkey detected (Ctrl+Alt+W recognized)
  P2: Latency acceptable (hotkey → recording_start ≤ 100ms)
  P3: Audio recorded (≥ 0.5s)
  P4: Silence detection works (stops at 1.5s+ silence)
  P5: Transcription completes (result is valid UTF-8)
  P6: Clipboard write succeeds
  P7: No crashes on 10 consecutive uses
  
Dev automated tests:
  pytest test_hotkey.py::test_detection (10 hotkeys, all detected)
  pytest test_latency.py (measure timings)
  pytest test_audio.py (check duration)
  pytest test_silence.py (verify silence threshold)
  pytest test_transcribe.py (check output encoding)
  pytest test_clipboard.py (verify paste works)
  pytest test_stress.py (10 runs, no crashes)
  
Engineer performance metrics:
  Before deployment, measure:
  - CPU usage: average ≤ 30%, peak ≤ 50%
  - RAM usage: ≤ 2GB peak
  - Latency: 50-100ms (hotkey to recording start)
  - Reliability: 0 crashes in 10 runs
```

**Definition of done is non-negotiable. Don't ship without all 7 predicates true.**

---

## A20 — DECOMPOSITION DOCUMENT (Formal + Practical + Resource)

**CS (Theory):** A decomposition document is a formal specification. Make it precise.

**Dev (Real):** Write it in a format you'll actually use (not a PDF, something searchable).

**Engineer (System):** Include resource requirements and constraints.

**Pattern:**
```
Whisper daemon decomposition (living document):

---
## A. CONCEPT
Hotkey-triggered voice-to-text daemon. Capture Ctrl+Alt+W, record, transcribe, clipboard output.

## B. SCOPE
IN: Hotkey, recording, transcription, clipboard
OUT: GUI, settings, cloud APIs, multiple hotkeys

## C. CONSTRAINTS
- Linux X11 only
- 2,100 token budget
- 4GB RAM, no GPU
- Single session preference

## D. CRITICAL QUESTIONS
Q1: Does pynput support global hotkey on X11?
    Answer: UNKNOWN (will test in POC)
    If NO: dead end
    If YES: proceed to Q2

Q2: Does python-xlib work as fallback?
    Answer: UNKNOWN (will test if pynput fails)
    If NO: dead end
    If YES: use as primary

## E. ASSUMPTIONS RANKED
Critical: pynput/X11 global hotkey works
High: Microphone accessible
High: 1.4GB Whisper model fits in RAM
Medium: Clipboard library available

## F. DEAD ENDS (stop if hit)
1. No library can capture Ctrl+Alt+W globally on X11
2. Token budget exceeded before phase 2 complete

## G. DEFINITION OF DONE (ALL required)
- Hotkey detects Ctrl+Alt+W
- Latency < 100ms
- Records minimum 0.5s
- Stops on 1.5s silence
- Transcription valid UTF-8
- Clipboard write succeeds
- 10 consecutive runs, 0 crashes

## H. PHASES & TOKEN BUDGET
Phase 1 (POC): 500 tokens, 1 hour
Phase 2 (Design alternatives): 400 tokens, 30 min
Phase 3 (Implement best path): 1,200 tokens, 2 hours
TOTAL: 2,100 tokens, 3.5 hours

## I. STATUS
Started: 2026-03-29
Current: Phase 1 (POC stage)
Next: Test pynput POC

---

This document is updated as you learn. Not locked in stone.
```

---

## Integration: ARCHITECT sits above APEX

```
Project request:
"Build a hotkey daemon for voice-to-text"

ARCHITECT (5 minutes):
  A1-A3: Extract concept, scope, constraints
  A4-A6: Ask critical questions
  A7-A12: Define decomposition, alternatives, prove feasibility
  A13-A20: Estimate budget, name dead ends, define success
  
  Output: Decomposition document (1 page)
  Decision: "Proceed to APEX? YES / NO / INFEASIBLE"
  
If PROCEED → APEX begins
If NO / INFEASIBLE → Stop, don't waste tokens on bad path

APEX (only if ARCHITECT says YES):
  E1-E25: Execute the plan
  
FORGE:
  F1-F13: Align and document
  
CIPHER:
  G1-G11: Integrity gates
```

---

## Real Example: Whisper Daemon (With ARCHITECT)

**Without ARCHITECT:**
- Start building immediately (bad)
- Hit dead end (pynput fails)
- Pivot (X11)
- Hit dead end again (keysym import)
- Waste $5, 4 hours
- Stop (forced by E17)

**With ARCHITECT:**
```
ARCHITECT Phase: 20 minutes, 300 tokens

A4 (Critical path): "Does pynput Listener support global hotkey?"
→ Quick research (GitHub issues, StackOverflow)
→ Answer: NO (open issue says "use platform-specific solution")
→ Decision: Skip pynput, go straight to X11

A11 (Suitability matrix): Compare libraries
→ pynput (55/100) < X11 (70/100) < evdev (65/100)
→ Choose: X11 first, evdev fallback

A13-A15: Budget
→ Phase 1 POC: 500 tokens (X11 + evdev POCs both)
→ Phase 2 Design: 400 tokens
→ Phase 3 Impl: 1,200 tokens
→ Total: 2,100 tokens
→ If exceed by phase 2: Stop

A10 (POC scope): Test only the critical path
→ DON'T load Whisper in POC (wastes time)
→ Only test X11 hotkey detection
→ Cost: 200 tokens instead of 1,000

ARCHITECT Output: "Proceed with X11 path. Budget 2,100 tokens. POC scope: X11 detection only."

APEX Phase: Starts with clear constraints
```

**Result:** Start with right path immediately. No pynput detour. Only pay cost of X11 (if it works) or evdev fallback (if X11 fails). Saves $3-4 and 2-3 hours.

---

## ARCHITECT as a Discipline

Every project ≥ 2,000 tokens must start with ARCHITECT.
Every project with unknown dependencies must start with ARCHITECT.
Every project with multiple viable approaches must start with ARCHITECT.

Cost: 5-10% of total project tokens.
Benefit: 40-60% reduction in wasted tokens.

This is CS (theory) + Dev (practice) + Engineer (resource awareness) working together.

