"""Setup configuration for sdocx2md"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sdocx2md",
    version="0.1.0",
    author="zerossin",
    author_email="zerossin@gmail.com",
    description="Convert DOCX/TXT files to Markdown with structured metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zerossin/sdocx2md",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-docx>=0.8.11",
    ],
    entry_points={
        "console_scripts": [
            "sdocx2md=sdocx2md.cli:main",
        ],
    },
)
