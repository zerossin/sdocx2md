# sdocx2md

삼성 노트 파일을 Markdown(`.md`)으로 변환해주는 Python CLI 도구입니다.

> **Note**: 다만 삼성 노트 파일은 Word 문서(`.docx`) 또는 텍스트 파일(`.txt`)로 추출하여 저장해야 합니다.

## 설치

### 소스에서 설치
```bash
git clone https://github.com/cherossin/sdocx2md
cd sdocx2md
pip install -e .
```

## 사용법

### 단일 파일 변환
```bash
sdocx2md input.txt output.md
```

### 디렉토리 재귀 변환
```bash
sdocx2md ./input_dir ./output_dir -r
```

## 파일명 형식

메타데이터 자동 추출을 위해 다음 형식을 권장합니다:
(삼성 노트에서 자동으로 정해주는 이름입니다.)

```
제목_YYMMDD_HHMMSS.확장자
```

예시:
- `회의록_250508_140000.docx` → 제목: 회의록, 날짜: 2025-05-08 14:00:00
- `보고서_250508_093045.txt` → 제목: 보고서, 날짜: 2025-05-08 09:30:45

## 출력 형식

### Markdown 파일
```markdown
---
title: 회의록
created_date: 2025-05-08
created_time: 14:00:00
---

회의 내용...

![image](회의록_assets/image1.png)
```

### 폴더 구조
```
output/
├── 회의록.md
├── 회의록_assets/
│   ├── image1.png
│   └── image2.jpg
└── subfolder/
    └── 보고서.md
```

## 옵션

- `-r, --recursive`: 디렉토리 재귀 변환
- `-v, --verbose`: 상세 로그 출력

## 지원 형식

- **입력**: `.txt`, `.md`, `.docx`
- **출력**: `.md` (Markdown)

## 요구사항

- Python 3.8+
- python-docx

## 라이센스

MIT License

## 관련 문서

- [English README](README.en.md)
- [Development Guide](DEVELOPMENT.md)
