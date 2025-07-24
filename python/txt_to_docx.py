from docx import Document
def txt_to_docx(input_path, output_path):
    document = Document()
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            document.add_paragraph(line.strip())
    document.save(output_path)