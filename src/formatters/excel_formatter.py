"""Excel formatter"""

import pandas as pd
from pathlib import Path
from src.formatters.base_formatter import BaseFormatter

class ExcelFormatter(BaseFormatter):
    """Generate Excel reports"""
    
    def generate(self, output_path: Path, **kwargs):
        """Generate Excel report"""
        self.validate_data()
        output_path = Path(output_path)
        
        # Create Excel writer
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            self.data.to_excel(writer, sheet_name='Data', index=False, **kwargs)
            
            # Add summary sheet
            summary_data = {
                'Metric': ['Total Rows', 'Total Columns', 'Generated From'],
                'Value': [len(self.data), len(self.data.columns), self.title]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        return output_path
