#!/usr/bin/env python3
"""
CHAMP v3 — Convert Here And Make Plaintext (Hybrid)
Batch PDF converter for Claude. Zero vision tokens. Handles text + image PDFs.

Modes:
  champ file1.pdf file2.pdf file3.pdf        → drag-drop (auto-detect mode)
  champ --dir /path/to/folder                → batch convert folder (auto-detect)
  champ file.pdf --out /output/path          → custom output folder
  champ file.pdf --mode text|ocr|images|auto → choose extraction mode (default: auto)
  champ file.pdf --chunk 100                 → chunk size (default 80 pages)
  champ file.pdf --stdout                    → print to stdout (text/OCR only, single file)
  champ file.pdf --grep "keyword"            → extract matching lines (text/OCR only)

Extraction modes:
  auto   → Detect PDF type. Text PDF → pdftotext. Image PDF → try OCR, fallback to images.
  text   → Force pdftotext (text PDFs only). Fails on scanned/image PDFs.
  ocr    → Force Tesseract OCR (scanned PDFs). Slower, requires tesseract installed.
  images → Extract images as .jpg files. Best for mixed content. No OCR.

Output:
  - Original PDFs copied to output folder (never modified)
  - Text: .txt files with extracted plaintext
  - OCR: .txt files with OCR'd text (slower, handles scanned PDFs)
  - Images: .jpg files extracted from PDF pages
  - Large PDFs (>80 pages) auto-chunked into page ranges
  - CHAMP_INDEX.md generated for navigation
"""

import sys
import os
import subprocess
import argparse
import shutil
import tempfile
from datetime import datetime


def get_page_count(pdf_path):
    """Get page count using pdfinfo."""
    try:
        result = subprocess.run(
            ['pdfinfo', pdf_path],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Pages:'):
                return int(line.split(':')[1].strip())
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return None
    return None


def detect_pdf_type(pdf_path):
    """
    Auto-detect if PDF is text-based or image-based (scanned).
    Returns: 'text' | 'image' | 'mixed' | 'unknown'
    """
    try:
        # Try text extraction on first page
        result = subprocess.run(
            ['pdftotext', '-f', '1', '-l', '1', pdf_path, '-'],
            capture_output=True, text=True, timeout=5
        )
        text_content = result.stdout.strip()

        if len(text_content) > 100:
            # Significant text extracted → likely text-based PDF
            return 'text'
        elif len(text_content) > 0:
            # Some text extracted → mixed content
            return 'mixed'
        else:
            # No text extracted → likely image-based (scanned)
            return 'image'
    except Exception:
        # Detection failed → assume image
        return 'unknown'


def extract_text(pdf_path, start_page=None, end_page=None):
    """Extract text from PDF using pdftotext. Page numbers are 1-indexed."""
    cmd = ['pdftotext', '-layout', pdf_path, '-']
    if start_page is not None and end_page is not None:
        cmd = ['pdftotext', '-layout', '-f', str(start_page), '-l', str(end_page), pdf_path, '-']

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"ERROR: pdftotext failed on {pdf_path}: {e.stderr}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("ERROR: pdftotext not installed. Run: sudo apt install poppler-utils", file=sys.stderr)
        sys.exit(1)


def extract_via_ocr(pdf_path, start_page=None, end_page=None):
    """Extract text from PDF using Tesseract OCR (for scanned PDFs)."""
    try:
        # Create temp directory for images
        with tempfile.TemporaryDirectory() as tmpdir:
            # Convert PDF pages to images
            if start_page is not None and end_page is not None:
                pages_arg = f"{start_page}-{end_page}"
            else:
                pages_arg = None

            img_cmd = ['pdftoppm', '-jpeg', pdf_path, os.path.join(tmpdir, 'page')]
            if pages_arg:
                img_cmd.extend(['-f', str(start_page), '-l', str(end_page)])

            subprocess.run(img_cmd, capture_output=True, check=True)

            # OCR each image
            ocr_text = []
            for img_file in sorted(os.listdir(tmpdir)):
                img_path = os.path.join(tmpdir, img_file)
                result = subprocess.run(
                    ['tesseract', img_path, 'stdout'],
                    capture_output=True, text=True, check=True
                )
                ocr_text.append(result.stdout)

            return '\n---PAGE BREAK---\n'.join(ocr_text)

    except FileNotFoundError as e:
        missing_tool = str(e).split("'")[1] if "'" in str(e) else "tesseract or pdftoppm"
        print(f"ERROR: {missing_tool} not installed. Run: sudo apt install tesseract-ocr poppler-utils", file=sys.stderr)
        return None
    except subprocess.CalledProcessError as e:
        print(f"ERROR: OCR failed on {pdf_path}: {e.stderr}", file=sys.stderr)
        return None


def extract_images(pdf_path, output_folder, start_page=None, end_page=None):
    """Extract images from PDF using pdfimages."""
    try:
        img_output_pattern = os.path.join(output_folder, 'page')
        cmd = ['pdfimages', '-jpeg', pdf_path, img_output_pattern]

        if start_page is not None and end_page is not None:
            cmd.extend(['-f', str(start_page), '-l', str(end_page)])

        subprocess.run(cmd, capture_output=True, check=True)

        # List extracted images
        images = [f for f in os.listdir(output_folder) if f.startswith('page') and f.endswith('.jpg')]
        return images

    except FileNotFoundError:
        print("ERROR: pdfimages not installed. Run: sudo apt install poppler-utils", file=sys.stderr)
        return None
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Image extraction failed on {pdf_path}: {e.stderr}", file=sys.stderr)
        return None


def process_pdf(pdf_path, output_folder, chunk_size=80, stdout=False, grep_term=None, mode='auto'):
    """
    Process a single PDF: copy + extract + chunk if needed.

    mode: 'auto' (detect), 'text' (pdftotext), 'ocr' (tesseract), 'images' (pdfimages)
    """

    if not os.path.exists(pdf_path):
        print(f"ERROR: File not found: {pdf_path}", file=sys.stderr)
        return None

    if not pdf_path.lower().endswith('.pdf'):
        print(f"ERROR: Not a PDF: {pdf_path}", file=sys.stderr)
        return None

    # Get page count
    page_count = get_page_count(pdf_path)

    # Create output folder if needed
    os.makedirs(output_folder, exist_ok=True)

    # Copy PDF to output folder
    pdf_filename = os.path.basename(pdf_path)
    pdf_copy_path = os.path.join(output_folder, pdf_filename)
    try:
        shutil.copy2(pdf_path, pdf_copy_path)
    except Exception as e:
        print(f"ERROR: Failed to copy {pdf_path}: {e}", file=sys.stderr)
        return None

    # Determine chunking
    if page_count is None:
        # Cannot determine page count - extract full PDF without page range
        print(f"WARNING: Could not determine page count for {pdf_path}, extracting full document", file=sys.stderr)
        chunks = [(None, None)]
    elif page_count <= chunk_size:
        # Single chunk — no need to split
        chunks = [(1, page_count)]
    else:
        # Multiple chunks
        chunks = []
        for start in range(1, page_count + 1, chunk_size):
            end = min(start + chunk_size - 1, page_count)
            chunks.append((start, end))

    # Determine extraction mode
    actual_mode = mode
    if mode == 'auto':
        pdf_type = detect_pdf_type(pdf_path)
        if pdf_type == 'text':
            actual_mode = 'text'
            print(f"CHAMP: {pdf_filename} — detected as TEXT PDF, using pdftotext", file=sys.stderr)
        elif pdf_type in ['image', 'unknown']:
            actual_mode = 'ocr'
            print(f"CHAMP: {pdf_filename} — detected as IMAGE PDF, attempting OCR", file=sys.stderr)
        else:  # mixed
            actual_mode = 'ocr'
            print(f"CHAMP: {pdf_filename} — detected as MIXED PDF, using OCR for complete extraction", file=sys.stderr)

    # Extract content based on mode
    output_files = []

    if actual_mode == 'images':
        # Image extraction mode
        images = extract_images(pdf_path, output_folder)
        if images:
            for img in images:
                img_path = os.path.join(output_folder, img)
                img_size = os.path.getsize(img_path)
                output_files.append({
                    'img_file': img,
                    'bytes': img_size,
                    'pages': 'see image'
                })
        else:
            print(f"ERROR: Failed to extract images from {pdf_filename}", file=sys.stderr)
            return None

    else:
        # Text or OCR extraction mode (chunks)
        for start, end in chunks:
            if actual_mode == 'ocr':
                text = extract_via_ocr(pdf_path, start, end)
            else:  # text
                text = extract_text(pdf_path, start, end)

            if text is None:
                continue

            # Apply grep if specified (text/OCR only)
            if grep_term:
                lines = text.splitlines()
                matches = []
                for i, line in enumerate(lines):
                    if grep_term.lower() in line.lower():
                        context_start = max(0, i - 2)
                        context_end = min(len(lines), i + 3)
                        matches.extend(lines[context_start:context_end])
                        matches.append('---')
                text = '\n'.join(matches) if matches else f"No matches for: {grep_term}"

            # If single chunk, use clean name. If multiple, use page range.
            base = pdf_filename[:-4] if pdf_filename.lower().endswith('.pdf') else pdf_filename
            if len(chunks) == 1:
                txt_filename = base + '.txt'
            else:
                txt_filename = f"{base}_p{start:03d}-{end:03d}.txt"

            txt_path = os.path.join(output_folder, txt_filename)

            # Handle stdout for single file only
            if stdout and len(chunks) == 1:
                print(text)
            else:
                with open(txt_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                output_files.append({
                    'txt_file': txt_filename,
                    'lines': text.count('\n'),
                    'chars': len(text),
                    'pages': f"{start}-{end}" if len(chunks) > 1 else "all"
                })

    return {
        'pdf_original': pdf_path,
        'pdf_copy': pdf_copy_path,
        'page_count': page_count or 0,
        'chunks': len(chunks),
        'output_files': output_files,
        'extraction_mode': actual_mode
    }


def create_index(output_folder, results):
    """Create CHAMP_INDEX.md for navigation."""
    index_path = os.path.join(output_folder, 'CHAMP_INDEX.md')

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('# CHAMP Index\n\n')
        f.write(f'**Generated:** {timestamp}\n\n')

        total_files = len(results)
        total_pages = sum(r['page_count'] for r in results)

        f.write(f'**Summary:** {total_files} PDF(s), {total_pages} total pages\n\n')

        f.write('## Files\n\n')

        for result in results:
            pdf_name = os.path.basename(result['pdf_copy'])
            pages = result['page_count']
            chunks = result['chunks']

            f.write(f'### {pdf_name}\n')
            f.write(f'- **Pages:** {pages}\n')
            f.write(f'- **Chunks:** {chunks}\n')
            f.write(f'- **Output files:**\n')

            for output in result['output_files']:
                f.write(f'  - `{output["txt_file"]}` ({output["lines"]} lines, {output["chars"]} chars, pages {output["pages"]})\n')

            f.write('\n')

    print(f"CHAMP: Index created at {index_path}")


def main():
    parser = argparse.ArgumentParser(
        description='CHAMP v3 — Batch PDF converter (text + image PDFs, zero vision tokens)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  champ file1.pdf file2.pdf file3.pdf       # Drag-drop (auto-detect mode)
  champ --dir ~/Documents                   # Batch convert (auto-detect)
  champ file.pdf --mode ocr                 # Force OCR extraction
  champ file.pdf --mode images              # Extract as JPG images
  champ file.pdf --out ~/output             # Custom output folder
  champ file.pdf --chunk 100                # Larger chunk size
  champ file.pdf --stdout                   # Print to stdout (text/OCR only)
  champ file.pdf --grep "keyword"           # Extract matching lines (text/OCR only)

Modes:
  auto   (default) → Auto-detect PDF type. Text → pdftotext. Image → OCR.
  text   → Force pdftotext (fast, text PDFs only)
  ocr    → Force Tesseract OCR (scanned PDFs, slower)
  images → Extract pages as JPEG images (best for mixed/complex layouts)
        '''
    )

    parser.add_argument('pdfs', nargs='*', help='PDF file(s) to convert')
    parser.add_argument('--dir', help='Batch convert all PDFs in folder (recursive)')
    parser.add_argument('--out', default='./extracted_text',
                        help='Output folder (default: ./extracted_text)')
    parser.add_argument('--mode', choices=['auto', 'text', 'ocr', 'images'], default='auto',
                        help='Extraction mode (default: auto-detect)')
    parser.add_argument('--chunk', type=int, default=80,
                        help='Chunk size in pages (default: 80)')
    parser.add_argument('--stdout', action='store_true',
                        help='Print to stdout (text/OCR only, single file only)')
    parser.add_argument('--grep', metavar='TERM',
                        help='Extract matching lines (text/OCR only, single file only)')

    args = parser.parse_args()

    # Determine what to process
    pdf_list = []

    if args.dir:
        # Batch mode: find all PDFs in folder (recursive)
        dir_path = os.path.expanduser(args.dir)
        if not os.path.isdir(dir_path):
            print(f"ERROR: Directory not found: {dir_path}", file=sys.stderr)
            sys.exit(1)

        pdf_list = []
        for root, _, files in os.walk(dir_path):
            for f in files:
                if f.lower().endswith('.pdf'):
                    pdf_list.append(os.path.join(root, f))

        if not pdf_list:
            print(f"WARNING: No PDFs found in {dir_path}", file=sys.stderr)
            sys.exit(0)

    elif args.pdfs:
        # Drag-drop or explicit args
        pdf_list = args.pdfs
    else:
        parser.print_help()
        sys.exit(1)

    # Process all PDFs
    results = []
    output_folder = os.path.expanduser(args.out)

    # Warn if batch mode will ignore single-file-only flags
    if len(pdf_list) > 1:
        if args.stdout:
            print("WARNING: --stdout is single-file only, ignored in batch mode", file=sys.stderr)
        if args.grep:
            print(f"WARNING: --grep is single-file only, ignored in batch mode", file=sys.stderr)

    # Track failures
    failed = 0
    for pdf_path in pdf_list:
        result = process_pdf(
            pdf_path,
            output_folder,
            chunk_size=args.chunk,
            stdout=args.stdout and len(pdf_list) == 1,  # stdout only for single file
            grep_term=args.grep if len(pdf_list) == 1 else None,  # grep only for single file
            mode=args.mode
        )
        if result:
            results.append(result)
            pdf_name = os.path.basename(result['pdf_copy'])
            pages = result['page_count'] if result['page_count'] else "unknown"
            mode_str = result.get('extraction_mode', 'unknown')
            print(f"CHAMP: {pdf_name} ({pages} pages, {result['chunks']} chunk(s), mode: {mode_str})")
        else:
            failed += 1

    # Create index if batch or multi-file
    if len(pdf_list) > 1 or args.dir:
        create_index(output_folder, results)

    if results:
        print(f"\nCHAMP: {len(results)} file(s) processed to {output_folder}")
    if failed:
        print(f"CHAMP: {failed} file(s) failed — see errors above", file=sys.stderr)


if __name__ == '__main__':
    main()
