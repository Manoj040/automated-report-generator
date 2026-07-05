# Automated Report Generator

A powerful and flexible Python tool for generating professional reports in multiple formats (PDF, HTML, Excel, CSV) from various data sources.

## Features

✨ **Multi-Format Output**
- Generate reports in PDF, HTML, Excel, and CSV formats
- Professional styling and formatting
- Customizable templates and layouts

📊 **Multiple Data Sources**
- Load data from CSV files
- Import from Excel spreadsheets
- Parse JSON data
- Auto-format detection

🔧 **Flexible Configuration**
- JSON-based configuration system
- Environment variable support
- Customizable output directories
- Batch report generation

🧪 **Production Ready**
- Comprehensive unit tests
- Error handling and validation
- Modular architecture
- Clean, maintainable code

📚 **Easy to Use**
- Simple API
- Extensive examples
- Well-documented code
- Ready-to-run scripts

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Manoj040/automated-report-generator.git
cd automated-report-generator
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run examples**
```bash
python examples/example_usage.py
```

## Usage

### Basic Example

```python
from src.data_loader import DataLoader
from src.report_generator import ReportGenerator

# Load data
loader = DataLoader()
data = loader.load_csv('data.csv')

# Create report generator
generator = ReportGenerator(data, title="My Report")

# Generate reports
generator.generate_pdf('report.pdf')
generator.generate_html('report.html')
generator.generate_excel('report.xlsx')
generator.generate_csv('report.csv')
```

### Generate All Formats at Once

```python
# Generate all formats with one call
results = generator.generate_all('my_report')

# results = {
#     'pdf': {'status': 'success', 'path': 'output/my_report.pdf'},
#     'html': {'status': 'success', 'path': 'output/my_report.html'},
#     'excel': {'status': 'success', 'path': 'output/my_report.xlsx'},
#     'csv': {'status': 'success', 'path': 'output/my_report.csv'}
# }
```

### Auto-Detect File Format

```python
# Automatically detect and load any supported format
loader = DataLoader()
data = loader.detect_and_load('data.xlsx')  # Works with CSV, Excel, JSON too
```

### Load Different Formats

```python
# Load CSV
data = loader.load_csv('data.csv')

# Load Excel
data = loader.load_excel('data.xlsx', sheet_name=0)

# Load JSON
data = loader.load_json_to_dataframe('data.json')
```

### Get Data Summary

```python
# Get summary statistics
summary = generator.get_summary()
print(f"Rows: {summary['rows']}")
print(f"Columns: {summary['columns']}")
print(f"Column Names: {summary['columns_list']}")
```

## Project Structure

```
automated-report-generator/
├── src/
│   ├── __init__.py
│   ├── config.py              # Configuration management
│   ├── data_loader.py         # Data loading module
│   ├── report_generator.py    # Main report generation
│   └── formatters/            # Format-specific generators
│       ├── __init__.py
│       ├── base_formatter.py  # Abstract base class
│       ├── pdf_formatter.py   # PDF generation
│       ├── html_formatter.py  # HTML generation
│       ├── excel_formatter.py # Excel generation
│       └── csv_formatter.py   # CSV generation
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py    # Data loader tests
│   └── test_report_generator.py # Generator tests
├── examples/
│   ├── example_usage.py       # Usage examples
│   ├── sample_data.csv        # Sample data
│   └── sample_config.json     # Sample configuration
├── requirements.txt           # Project dependencies
├── setup.py                   # Package setup
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Configuration

### Using Config Class

```python
from src.config import Config

# Access configuration
print(Config.OUTPUT_DIR)      # Output directory
print(Config.DEFAULT_FORMAT)  # Default report formats
print(Config.TITLE)           # Default report title
```

### Load from JSON Config

```python
config = Config.load_from_file('examples/sample_config.json')
print(config)
```

### Sample Config File

```json
{
  "report": {
    "title": "Monthly Sales Report",
    "formats": ["pdf", "html", "excel", "csv"],
    "schedule": "monthly"
  },
  "data": {
    "source": "data.csv",
    "type": "csv",
    "encoding": "utf-8"
  },
  "output": {
    "directory": "./output",
    "filename_format": "report_{timestamp}"
  }
}
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_data_loader.py

# Run with coverage
python -m pytest tests/ --cov=src
```

## Examples

### Example 1: Generate Basic Report

```bash
python examples/example_usage.py
```

This runs all 4 example scenarios and generates sample reports.

### Example 2: Custom Report

```python
from src.data_loader import DataLoader
from src.report_generator import ReportGenerator

# Load your data
loader = DataLoader()
data = loader.detect_and_load('your_data.csv')

# Create custom report
generator = ReportGenerator(data, title="Custom Report Title")

# Generate all formats
results = generator.generate_all('custom_report')

# Check results
for fmt, result in results.items():
    print(f"{fmt}: {result['status']}")
```

### Example 3: Batch Processing

```python
from pathlib import Path
from src.data_loader import DataLoader
from src.report_generator import ReportGenerator

# Process multiple files
data_dir = Path('data')
for csv_file in data_dir.glob('*.csv'):
    data = DataLoader().load_csv(csv_file)
    generator = ReportGenerator(data, title=csv_file.stem)
    generator.generate_all(csv_file.stem)
    print(f"Generated reports for {csv_file.name}")
```

## Supported Formats

### Input Formats
- ✅ CSV (Comma Separated Values)
- ✅ Excel (.xlsx, .xls)
- ✅ JSON

### Output Formats
- ✅ PDF (Professional, styled tables)
- ✅ HTML (Web-ready, responsive design)
- ✅ Excel (.xlsx with multiple sheets)
- ✅ CSV (Data export)

## Dependencies

- **pandas**: Data manipulation and analysis
- **reportlab**: PDF generation
- **openpyxl**: Excel file handling
- **jinja2**: Template engine
- **schedule**: Task scheduling
- **python-dotenv**: Environment variable management
- **pillow**: Image processing
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization

See `requirements.txt` for version details.

## Advanced Usage

### Custom Formatter

Create your own formatter by extending `BaseFormatter`:

```python
from src.formatters.base_formatter import BaseFormatter
from pathlib import Path

class CustomFormatter(BaseFormatter):
    def generate(self, output_path: Path, **kwargs):
        self.validate_data()
        # Your custom generation logic here
        return output_path
```

### Error Handling

```python
from src.data_loader import DataLoader
from src.report_generator import ReportGenerator

try:
    loader = DataLoader()
    data = loader.load_csv('data.csv')
    generator = ReportGenerator(data)
    results = generator.generate_all('report')
except ValueError as e:
    print(f"Data error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Tips

1. **Use batch processing** for multiple files
2. **Pre-filter data** before generating reports
3. **Cache loaded data** if generating multiple formats
4. **Use appropriate data types** in your source files
5. **Monitor memory** for large datasets

## Troubleshooting

### Issue: "Module not found" error
**Solution**: Ensure you're running from the project root directory and have installed dependencies.
```bash
pip install -r requirements.txt
```

### Issue: Permission denied when writing files
**Solution**: Ensure the output directory exists and is writable.
```bash
mkdir -p output
chmod 755 output
```

### Issue: Memory error with large files
**Solution**: Process data in chunks or filter before generating reports.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Manoj040** - Created this automated report generation tool

## Support

For issues, questions, or suggestions, please:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include error messages and sample data

## Roadmap

Planned features:
- [ ] Email scheduling integration
- [ ] Database source support
- [ ] Chart and graph generation
- [ ] Custom template support
- [ ] API endpoint wrapper
- [ ] Docker containerization
- [ ] Cloud storage integration
- [ ] Real-time report streaming

## Changelog

### v0.1.0 (2024)
- Initial release
- Support for CSV, Excel, JSON input
- PDF, HTML, Excel, CSV output formats
- Configuration management
- Unit tests included
- Example usage scripts

## Related Projects

- [pandas](https://github.com/pandas-dev/pandas) - Data manipulation
- [reportlab](https://www.reportlab.com/) - PDF generation
- [openpyxl](https://openpyxl.readthedocs.io/) - Excel handling

---

Made with ❤️ by Manoj040
