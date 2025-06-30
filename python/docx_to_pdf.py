from docx2pdf import convert
import os

def docx_to_pdf(input_path, output_path):
    # Se for um arquivo único, converte diretamente
    if os.path.isfile(input_path):
        convert(input_path, output_path)
    else:
        raise ValueError("Caminho inválido para arquivo DOCX.")