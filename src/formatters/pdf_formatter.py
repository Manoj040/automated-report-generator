"""PDF formatter"""

import pandas as pd
from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from src.formatters.base_formatter import BaseFormatter

class PDFFormatter(BaseFormatter):
    """Generate PDF reports"""
    
    def generate(self, output_path: Path, page_size=letter, **kwargs):
        """Generate PDF report"""
        self.validate_data()
        output_path = Path(output_path)
        
        # Create PDF document
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=page_size,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        # Create story (content)
        story = []
        styles = getSampleStyleSheet()
        
        # Add title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#007bff'),
            spaceAfter=12,
            alignment=1  # Center
        )
        story.append(Paragraph(self.title, title_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Add summary
        summary_style = ParagraphStyle(
            'Summary',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.grey
        )
        summary_text = f"Total Records: {len(self.data)} | Total Columns: {len(self.data.columns)}"
        story.append(Paragraph(summary_text, summary_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Add data table
        table_data = [list(self.data.columns)] + self.data.values.tolist()
        table = Table(table_data, repeatRows=1)
        
        # Style table
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#007bff')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ]))
        
        story.append(table)
        
        # Build PDF
        doc.build(story)
        
        return output_path
