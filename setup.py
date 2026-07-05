from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='automated-report-generator',
    version='0.1.0',
    author='Manoj040',
    description='Automated Report Generator - Generate reports in multiple formats from file sources',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Manoj040/automated-report-generator',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'pandas>=1.3.0',
        'reportlab>=3.6.0',
        'openpyxl>=3.7.0',
        'jinja2>=3.0.0',
        'schedule>=1.1.0',
        'requests>=2.26.0',
        'python-dotenv>=0.19.0',
        'pillow>=8.3.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
    ],
)
