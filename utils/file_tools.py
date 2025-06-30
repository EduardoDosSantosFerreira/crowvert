import os
import shutil
import tempfile

def create_temp_dir(prefix="temp_convert_"):
    """
    Cria um diretório temporário e retorna o caminho.
    """
    return tempfile.mkdtemp(prefix=prefix)

def remove_dir(path):
    """
    Remove um diretório e todo seu conteúdo.
    """
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

def is_valid_file(path, extensions=None):
    """
    Verifica se o arquivo existe e se sua extensão está na lista permitida.
    Se extensions for None, só verifica se o arquivo existe.
    """
    if not os.path.isfile(path):
        return False
    
    if extensions:
        ext = os.path.splitext(path)[1].lower()
        return ext in extensions
    return True

def change_extension(file_path, new_extension):
    """
    Retorna o caminho do arquivo com a nova extensão, sem alterar o arquivo físico.
    Exemplo: "arquivo.txt" + ".docx" -> "arquivo.docx"
    """
    base = os.path.splitext(file_path)[0]
    if not new_extension.startswith('.'):
        new_extension = '.' + new_extension
    return base + new_extension