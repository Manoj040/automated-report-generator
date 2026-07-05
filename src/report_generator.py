"""Core report generation module"""

import pandas as pd
from pathlib import Path
from typing import List, Optional
from src.formatters.pdf_formatter import PDFFormatter
from src.formatters.html_formatter import HTMLFormatter
from src.formatters.csv_formatter import CSVFormatter
from src.formatters.excel_formatter import ExcelFormatter
from src.config import Config

class ReportGenerator:
    """Generate reports in multiple formats"""
    
    def __init__(self, data: pd.DataFrame, title: str = 'Report'):
        self.data = data
        self.title = title
        self.output_dir = Config.OUTPUT_DIR
        
    def generate_pdf(self, filename: str, **kwargs) -> Path:
        """Generate PDF report"""
        output_path = self.output_dir / filename
        formatter = PDFFormatter(self.data, self.title)
        formatter.generate(output_path, **kwargs)
        return output_path
    
    def generate_html(self, filename: str, **kwargs) -> Path:
        """Generate HTML report"""
        output_path = self.output_dir / filename
        formatter = HTMLFormatter(self.data, self.title)
        formatter.generate(output_path, **kwargs)
        return output_path
    
    def generate_excel(self, filename: str, **kwargs) -> Path:
        """Generate Excel report"""
        output_path = self.output_dir / filename
        formatter = ExcelFormatter(self.data, self.title)
        formatter.generate(output_path, **kwargs)
        return output_path
    
    def generate_csv(self, filename: str, **kwargs) -> Path:
        """Generate CSV report"""
        output_path = self.output_dir / filename
        formatter = CSVFormatter(self.data, self.title)
        formatter.generate(output_path, **kwargs)
        return output_path
    
    def generate_all(self, base_filename: str, formats: List[str] = None) -> dict:
        """Generate reports in all specified formats"""
        if formats is None:
            formats = Config.DEFAULT_FORMAT
        
        results = {}
        base_name = Path(base_filename).stem
        
        format_map = {
            'pdf': self.generate_pdf,
            'html': self.generate_html,
            'excel': self.generate_excel,
            'csv': self.generate_csv,
        }
        
        for fmt in formats:
            if fmt.lower() in format_map:
                try:
                    filename = f"{base_name}.{fmt.lower()}"
                    if fmt.lower() == 'excel':
                        filename = f"{base_name}.xlsx"
                    path = format_map[fmt.lower()](filename)
                    results[fmt] = {'status': 'success', 'path': str(path)}
                except Exception as e:
                    results[fmt] = {'status': 'error', 'message': str(e)}
            else:
                results[fmt] = {'status': 'error', 'message': f'Unsupported format: {fmt}'}
        
        return results
    
    def get_summary(self) -> dict:
        """Get summary statistics of the data"""
        return {
            'rows': len(self.data),
            'columns': len(self.data.columns),
            'columns_list': list(self.data.columns),
            'dtypes': self.data.dtypes.to_dict(),
        }
