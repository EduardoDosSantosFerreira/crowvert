from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os
def docx_to_pdf(input_path, output_path=None):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + ".pdf"
        doc = Document(input_path)
        c = canvas.Canvas(output_path, pagesize=A4)
        width, height = A4
        margin = 2.5 * cm
        x = margin
        y = height - margin
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_LEFT))
        for para in doc.paragraphs:
            if para.alignment == 1:    
                style = ParagraphStyle('Center', parent=styles['Normal'], alignment=TA_CENTER)
            elif para.alignment == 2:  
                style = ParagraphStyle('Right', parent=styles['Normal'], alignment=TA_RIGHT)
            else:                      
                style = styles['Normal']
            text = []
            for run in para.runs:
                run_text = run.text
                if run.bold:
                    run_text = f"<b>{run_text}</b>"
                if run.italic:
                    run_text = f"<i>{run_text}</i>"
                if run.underline:
                    run_text = f"<u>{run_text}</u>"
                text.append(run_text)
            full_text = ''.join(text)
            p = Paragraph(full_text, style)
            p.wrapOn(c, width - 2*margin, height)
            if y - p.height < margin:
                c.showPage()
                y = height - margin
            p.drawOn(c, x, y - p.height)
            y -= p.height + (0.5 * cm)
        c.save()
        print(f"Documento convertido com sucesso: {output_path}")
        return True
    except Exception as e:
        print(f"Erro na conversão: {str(e)}")
        return False