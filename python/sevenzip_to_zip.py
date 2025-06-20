import os
import py7zr
import zipfile

def sevenzip_to_zip(input_path, output_path):
    """
    Converte um arquivo .7z para .zip.
    
    Parâmetros:
    - input_path: caminho do arquivo .7z de entrada
    - output_path: caminho do arquivo .zip de saída
    """

    # Criar uma pasta temporária para extrair os arquivos do .7z
    temp_dir = input_path + "_temp_extracted"

    try:
        # Extrair o conteúdo do .7z
        with py7zr.SevenZipFile(input_path, mode='r') as archive:
            archive.extractall(path=temp_dir)

        # Criar o arquivo .zip com os arquivos extraídos
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    # Adiciona o arquivo no zip com o caminho relativo
                    rel_path = os.path.relpath(full_path, temp_dir)
                    zipf.write(full_path, rel_path)
    finally:
        # Remover a pasta temporária
        import shutil
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
