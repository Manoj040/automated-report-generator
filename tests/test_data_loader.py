"""Tests for data loader"""

import unittest
import pandas as pd
from pathlib import Path
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    """Test cases for DataLoader class"""
    
    def setUp(self):
        self.loader = DataLoader()
    
    def test_load_csv(self):
        """Test CSV loading"""
        df = self.loader.load_csv('examples/sample_data.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
    
    def test_load_nonexistent_file(self):
        """Test loading non-existent file"""
        with self.assertRaises(ValueError):
            self.loader.load_csv('nonexistent.csv')
    
    def test_detect_and_load(self):
        """Test auto-detection of file format"""
        df = self.loader.detect_and_load('examples/sample_data.csv')
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
