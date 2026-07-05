"""Configuration management for the report generator"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration class"""
    
    # Project paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / 'data'
    OUTPUT_DIR = BASE_DIR / 'output'
    TEMPLATES_DIR = BASE_DIR / 'src' / 'templates'
    
    # Report settings
    DEFAULT_FORMAT = ['pdf', 'html', 'csv', 'excel']
    TITLE = 'Automated Report'
    INCLUDE_CHARTS = True
    
    # Data loading settings
    ENCODING = 'utf-8'
    
    # Scheduling
    SCHEDULE_ENABLED = False
    SCHEDULE_TIME = '09:00'  # HH:MM format
    
    @classmethod
    def load_from_file(cls, config_path):
        """Load configuration from JSON file"""
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
        return config_data
    
    @classmethod
    def ensure_directories(cls):
        """Create necessary directories if they don't exist"""
        cls.DATA_DIR.mkdir(exist_ok=True)
        cls.OUTPUT_DIR.mkdir(exist_ok=True)
        cls.TEMPLATES_DIR.mkdir(exist_ok=True)

Config.ensure_directories()
