"""HTML formatter"""

import pandas as pd
from pathlib import Path
from jinja2 import Template
from src.formatters.base_formatter import BaseFormatter
from src.config import Config

class HTMLFormatter(BaseFormatter):
    """Generate HTML reports"""
    
    def generate(self, output_path: Path, include_styles: bool = True, **kwargs):
        """Generate HTML report"""
        self.validate_data()
        output_path = Path(output_path)
        
        # Convert DataFrame to HTML
        table_html = self.data.to_html(classes='table', index=False)
        
        # Create HTML content
        html_content = self._create_html(table_html, include_styles)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_path
    
    def _create_html(self, table_html: str, include_styles: bool = True) -> str:
        """Create complete HTML document"""
        styles = """
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
            .summary { background: #f8f9fa; padding: 15px; margin: 20px 0; border-radius: 5px; }
            table { border-collapse: collapse; width: 100%; margin: 20px 0; }
            table, th, td { border: 1px solid #ddd; }
            th { background-color: #007bff; color: white; padding: 12px; text-align: left; }
            td { padding: 10px; }
            tr:nth-child(even) { background-color: #f8f9fa; }
            tr:hover { background-color: #e9ecef; }
            .timestamp { color: #666; font-size: 0.9em; }
        </style>
        """ if include_styles else ""
        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.title}</title>
            {styles}
        </head>
        <body>
            <h1>{self.title}</h1>
            <div class="summary">
                <p><strong>Total Rows:</strong> {len(self.data)}</p>
                <p><strong>Total Columns:</strong> {len(self.data.columns)}</p>
            </div>
            {table_html}
            <div class="timestamp">
                <p>Report generated automatically</p>
            </div>
        </body>
        </html>
        """
        return html
