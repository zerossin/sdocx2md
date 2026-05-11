# sdocx2md

A Python CLI tool that converts Samsung Notes files to Markdown(`.md`).

> **Note**: Samsung Notes files must be exported as Word documents (`.docx`) or text files (`.txt`) before conversion.

## Installation

### From source
```bash
git clone https://github.com/cherossin/sdocx2md
cd sdocx2md
pip install -e .
```

## Usage

### Convert a single file
```bash
sdocx2md input.txt output.md
```

### Convert a directory recursively
```bash
sdocx2md ./input_dir ./output_dir -r
```

## Filename Format

To automatically extract metadata, use the following naming convention:
(This format is automatically set by Samsung Notes)

```
Title_YYMMDD_HHMMSS.extension
```

Examples:
- `meeting_250508_140000.docx` → title: meeting, date: 2025-05-08 14:00:00
- `report_250508_093045.txt` → title: report, date: 2025-05-08 09:30:45

## Output Format

### Markdown File
```markdown
---
title: meeting
created_date: 2025-05-08
created_time: 14:00:00
---

Meeting content...

![image](meeting_assets/image1.png)
```

### Folder Structure
```
output/
├── meeting.md
├── meeting_assets/
│   ├── image1.png
│   └── image2.jpg
└── subfolder/
    └── report.md
```

## Options

- `-r, --recursive`: Convert directory recursively
- `-v, --verbose`: Enable verbose logging

## Supported Formats

- **Input**: `.txt`, `.md`, `.docx`
- **Output**: `.md` (Markdown)

## Requirements

- Python 3.8+
- python-docx

## Features

✅ DOCX/TXT to Markdown conversion  
✅ Automatic image extraction from DOCX files  
✅ Automatic metadata extraction from filename  
✅ Directory hierarchy preservation  
✅ YAML front matter generation  
✅ Priority handling for duplicate files (.docx preferred over .txt)

## License

MIT License

## Related Documentation

- [한국어 README](README.md)
- [Development Guide](DEVELOPMENT.md)
