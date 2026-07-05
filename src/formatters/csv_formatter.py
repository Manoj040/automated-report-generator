"""CSV formatter"""

import pandas as pd
from pathlib import Path
from src.formatters.base_formatter import BaseFormatter

class CSVFormatter(BaseFormatter):
    """Generate CSV reports"""
    
    def generate(self, output_path: Path, **kwargs):
        """Generate CSV report"""
        self.validate_data()
        output_path = Path(output_path)
        
        # Add title as comment if specified
        with open(output_path, 'w') as f:
            f.write(f"# {self.title}\n")
        
        # Append CSV data
        self.data.to_csv(output_path, mode='a', index=False, **kwargs)
        
        return output_path
