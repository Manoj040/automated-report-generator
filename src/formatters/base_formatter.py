"""Base formatter class"""

import pandas as pd
from abc import ABC, abstractmethod
from pathlib import Path

class BaseFormatter(ABC):
    """Abstract base class for all formatters"""
    
    def __init__(self, data: pd.DataFrame, title: str = 'Report'):
        self.data = data
        self.title = title
    
    @abstractmethod
    def generate(self, output_path: Path, **kwargs):
        """Generate report in specific format"""
        pass
    
    def validate_data(self):
        """Validate that data exists and is valid"""
        if self.data is None or self.data.empty:
            raise ValueError("Data is empty or None")
