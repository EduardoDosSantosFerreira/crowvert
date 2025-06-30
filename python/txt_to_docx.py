from docx import Document

def txt_to_docx(input_path, output_path):
    """
    Converte um arquivo .txt para .docx.
    
    Parâmetros:
    - input_path: caminho do arquivo .txt de entrada
    - output_path: caminho do arquivo .docx de saída
    """
    # Criar um novo documento
    document = Document()
    
    # Abrir o arquivo .txt e ler linha por linha
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Adicionar cada linha como um parágrafo no documento
            document.add_paragraph(line.strip())
    
    # Salvar o documento .docx
    document.save(output_path)