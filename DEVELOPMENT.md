# sdocx2md Development Notes

## Project Structure

```
sdocx2md/
├── sdocx2md/           # Main package
│   ├── __init__.py
│   ├── cli.py          # CLI entry point
│   ├── parser.py       # Filename parsing & frontmatter generation
│   ├── converter.py    # File/directory conversion logic
│   └── ...
├── tests/              # Unit tests
├── examples/           # Example files
├── setup.py            # Package installation
├── requirements.txt    # Dependencies
└── README.md
```

## Key Features

- **Title Extraction**: Parses `Title_YYMMDD_HHMMSS` format to extract title
- **Metadata**: Automatically parses creation date and time
- **Image Extraction**: Extracts images from DOCX files to `{title}_assets/` folder
- **Directory Hierarchy**: Preserves folder structure during batch conversion
- **File Priority**: When both `.txt` and `.docx` exist with same name, `.docx` is prioritized
- **Minimal Metadata**: Only stores title, date, and time in YAML frontmatter

## Development Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `./venv/Scripts/activate` (Windows)
4. Install in development mode: `pip install -e .`
5. Run tests: `python -m pytest tests/`

## Key Components

### Parser Module (`parser.py`)
- `parse_filename()`: Extracts title and metadata from filenames
- `generate_frontmatter()`: Creates YAML frontmatter for markdown files

### Converter Module (`converter.py`)
- `FileConverter`: Handles single file conversion
  - Supports `.txt`, `.md`, `.docx` formats
  - Extracts text, tables, and images from DOCX files
  - Saves images to `{output_filename}_assets/` folder
  - References images in markdown using relative paths
  
- `DirectoryConverter`: Handles recursive directory conversion
  - Preserves directory hierarchy
  - Implements file priority logic (DOCX > TXT for same title)
  - Output filename: `{title}.md`
  - Creates `{title}_assets/` folder for each DOCX with images

### CLI Module (`cli.py`)
- Command-line interface with argparse
- Supports single file and batch directory conversion
- Logging support (verbose mode available)

## Output Format

All converted files include YAML frontmatter:
```yaml
---
title: DocumentTitle
created_date: YYYY-MM-DD
created_time: HH:MM:SS
---
```

## Testing

Run unit tests:
```bash
python -m pytest tests/ -v
```

Test specific module:
```bash
python -m pytest tests/test_parser.py -v
```

## Next Steps

- [ ] Add integration tests
- [ ] Support for `.doc` files (legacy Word format)
- [ ] Support for PDF files
- [ ] Configuration file support (`.sdocx2mdrc`)
- [ ] Better table formatting with alignment
- [ ] Support for embedded hyperlinks
- [ ] Support for text formatting (bold, italic, underline)
- [ ] Batch filename patterns configuration
