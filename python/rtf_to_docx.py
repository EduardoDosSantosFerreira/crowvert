# python/rtf_to_docx.py
import pypandoc
import os

def rtf_to_docx(input_path, output_path):
    """
    Converte arquivo RTF para DOCX usando pandoc
    :param input_path: Caminho do arquivo RTF de entrada
    :param output_path: Caminho do arquivo DOCX de saída
    """
    try:
        # Converte RTF para DOCX
        output = pypandoc.convert_file(
            input_path,
            'docx',
            outputfile=output_path,
            format='rtf'
        )
        
        if not os.path.exists(output_path):
            raise Exception("Arquivo de saída não foi criado")
            
    except Exception as e:
        raise Exception(f"Falha na conversão RTF para DOCX: {str(e)}")