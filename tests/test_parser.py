"""Tests for sdocx2md parser module"""

import pytest
from pathlib import Path
from sdocx2md.parser import parse_filename, generate_frontmatter


class TestParseFilename:
    """Test filename parsing functionality"""
    
    def test_standard_format(self):
        """Test parsing standard format: Title_YYMMDD_HHMMSS.txt"""
        title, meta = parse_filename("Notes_180305_192248.txt")
        
        assert title == "Notes"
        assert meta['created_date'] == "2018-03-05"
        assert meta['created_time'] == "19:22:48"
    
    def test_standard_format_without_extension(self):
        """Test parsing without extension"""
        title, meta = parse_filename("Report_221215_100530")
        
        assert title == "Report"
        assert meta['created_date'] == "2022-12-15"
        assert meta['created_time'] == "10:05:30"
    
    def test_invalid_format(self):
        """Test filename that doesn't match pattern"""
        title, meta = parse_filename("SomeRandomFile.txt")
        
        assert title == "SomeRandomFile"
        assert meta == {}
    
    def test_title_with_underscores(self):
        """Test title containing underscores"""
        title, meta = parse_filename("My_Long_Title_180305_192248.txt")
        
        assert title == "My_Long_Title"
        assert meta['created_date'] == "2018-03-05"
    
    def test_edge_case_year_parsing(self):
        """Test year parsing for different decades"""
        # 1990s
        title, meta = parse_filename("Old_951201_120000.txt")
        assert meta['created_date'] == "1995-12-01"
        
        # 2000s
        title, meta = parse_filename("New_050101_000000.txt")
        assert meta['created_date'] == "2005-01-01"
    
    def test_frontmatter_generation(self):
        """Test YAML frontmatter generation"""
        title = "Notes"
        meta = {'created_date': '2018-03-05', 'created_time': '19:22:48'}
        
        frontmatter = generate_frontmatter(title, meta)
        
        assert '---' in frontmatter
        assert 'title: Notes' in frontmatter
        assert 'created_date: 2018-03-05' in frontmatter
        assert 'created_time: 19:22:48' in frontmatter
        assert 'source:' not in frontmatter


if __name__ == '__main__':
    pytest.main([__file__])
