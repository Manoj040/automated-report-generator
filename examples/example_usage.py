#!/usr/bin/env python
"""Example usage of the Automated Report Generator"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import DataLoader
from src.report_generator import ReportGenerator
from src.config import Config

def example_1_basic_report():
    """Example 1: Generate a basic report in all formats"""
    print("\n=== Example 1: Basic Report Generation ===")
    
    # Load data
    loader = DataLoader()
    data = loader.load_csv('examples/sample_data.csv')
    print(f"Loaded data with {len(data)} rows and {len(data.columns)} columns")
    
    # Create report generator
    generator = ReportGenerator(data, title="Sales Report - January 2024")
    
    # Generate reports in all formats
    results = generator.generate_all('sales_report')
    
    print("\nGeneration Results:")
    for fmt, result in results.items():
        if result['status'] == 'success':
            print(f"  ✓ {fmt.upper()}: {result['path']}")
        else:
            print(f"  ✗ {fmt.upper()}: {result['message']}")

def example_2_individual_formats():
    """Example 2: Generate reports in individual formats"""
    print("\n=== Example 2: Individual Format Generation ===")
    
    loader = DataLoader()
    data = loader.load_csv('examples/sample_data.csv')
    
    generator = ReportGenerator(data, title="Product Analysis")
    
    # Generate each format individually
    pdf_path = generator.generate_pdf('product_analysis.pdf')
    print(f"PDF Report: {pdf_path}")
    
    html_path = generator.generate_html('product_analysis.html')
    print(f"HTML Report: {html_path}")
    
    excel_path = generator.generate_excel('product_analysis.xlsx')
    print(f"Excel Report: {excel_path}")
    
    csv_path = generator.generate_csv('product_analysis.csv')
    print(f"CSV Report: {csv_path}")

def example_3_auto_detect():
    """Example 3: Auto-detect file format"""
    print("\n=== Example 3: Auto-detect File Format ===")
    
    loader = DataLoader()
    # Let the loader detect the file type
    data = loader.detect_and_load('examples/sample_data.csv')
    print(f"Auto-loaded data: {len(data)} rows, {len(data.columns)} columns")
    
    generator = ReportGenerator(data, title="Auto-Detected Report")
    html_path = generator.generate_html('auto_report.html')
    print(f"Generated report: {html_path}")

def example_4_data_summary():
    """Example 4: Get data summary"""
    print("\n=== Example 4: Data Summary ===")
    
    loader = DataLoader()
    data = loader.load_csv('examples/sample_data.csv')
    
    generator = ReportGenerator(data, title="Data Summary")
    summary = generator.get_summary()
    
    print(f"\nSummary:")
    print(f"  Rows: {summary['rows']}")
    print(f"  Columns: {summary['columns']}")
    print(f"  Column Names: {summary['columns_list']}")

if __name__ == '__main__':
    print(f"Output directory: {Config.OUTPUT_DIR}")
    
    try:
        example_1_basic_report()
        example_2_individual_formats()
        example_3_auto_detect()
        example_4_data_summary()
        
        print("\n✓ All examples completed successfully!")
        print(f"Check the output directory: {Config.OUTPUT_DIR}")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
