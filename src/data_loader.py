"""Data loading module for various file formats"""

import pandas as pd
import json
from pathlib import Path
from typing import Union, List, Dict, Any

class DataLoader:
    """Load data from various file sources"""
    
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding
    
    def load_csv(self, filepath: str) -> pd.DataFrame:
        """Load data from CSV file"""
        try:
            return pd.read_csv(filepath, encoding=self.encoding)
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {e}")
    
    def load_excel(self, filepath: str, sheet_name: Union[str, int] = 0) -> pd.DataFrame:
        """Load data from Excel file"""
        try:
            return pd.read_excel(filepath, sheet_name=sheet_name)
        except Exception as e:
            raise ValueError(f"Error loading Excel file: {e}")
    
    def load_json(self, filepath: str) -> Union[Dict, List]:
        """Load data from JSON file"""
        try:
            with open(filepath, 'r', encoding=self.encoding) as f:
                return json.load(f)
        except Exception as e:
            raise ValueError(f"Error loading JSON file: {e}")
    
    def load_json_to_dataframe(self, filepath: str) -> pd.DataFrame:
        """Load JSON file and convert to DataFrame"""
        data = self.load_json(filepath)
        try:
            return pd.DataFrame(data)
        except Exception as e:
            raise ValueError(f"Error converting JSON to DataFrame: {e}")
    
    def detect_and_load(self, filepath: str) -> pd.DataFrame:
        """Automatically detect file type and load"""
        filepath = Path(filepath)
        extension = filepath.suffix.lower()
        
        if extension == '.csv':
            return self.load_csv(filepath)
        elif extension in ['.xlsx', '.xls']:
            return self.load_excel(filepath)
        elif extension == '.json':
            return self.load_json_to_dataframe(filepath)
        else:
            raise ValueError(f"Unsupported file format: {extension}")
