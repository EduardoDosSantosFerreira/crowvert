from docx import Document

def docx_to_txt(input_path, output_path):
    doc = Document(input_path)
    with open(output_path, "w", encoding="utf-8") as f:
        for para in doc.paragraphs:
            f.write(para.text + "\n")
