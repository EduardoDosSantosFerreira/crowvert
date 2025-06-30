from pdf2docx import Converter

def pdf_to_docx(input_path, output_path):
    converter = Converter(input_path)
    converter.convert(output_path)
    converter.close()