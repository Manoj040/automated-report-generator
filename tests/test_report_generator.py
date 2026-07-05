"""Tests for report generator"""

import unittest
import pandas as pd
from pathlib import Path
from src.report_generator import ReportGenerator
from src.data_loader import DataLoader
from src.config import Config

class TestReportGenerator(unittest.TestCase):
    """Test cases for ReportGenerator class"""
    
    def setUp(self):
        loader = DataLoader()
        self.data = loader.load_csv('examples/sample_data.csv')
        self.generator = ReportGenerator(self.data, title="Test Report")
    
    def test_initialization(self):
        """Test generator initialization"""
        self.assertEqual(self.generator.title, "Test Report")
        self.assertIsInstance(self.generator.data, pd.DataFrame)
    
    def test_get_summary(self):
        """Test data summary generation"""
        summary = self.generator.get_summary()
        self.assertIn('rows', summary)
        self.assertIn('columns', summary)
        self.assertEqual(summary['rows'], len(self.data))
    
    def test_generate_csv(self):
        """Test CSV generation"""
        output_path = self.generator.generate_csv('test_report.csv')
        self.assertTrue(output_path.exists())
        output_path.unlink()  # Clean up

if __name__ == '__main__':
    unittest.main()
