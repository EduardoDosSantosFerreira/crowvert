# python/rtf_to_pdf.py
import os
import sys
from tempfile import NamedTemporaryFile
import win32com.client  # pywin32
import pythoncom

def rtf_to_pdf(input_path: str, output_path: str) -> None:
    """
    Converte RTF para PDF usando Word via COM (Windows apenas)
    Funciona sem dependências externas além do pywin32 e Microsoft Word
    """
    if not os.path.exists(input_path):
        raise Exception(f"Arquivo não encontrado: {input_path}")
    
    if not input_path.lower().endswith('.rtf'):
        raise Exception("O arquivo de entrada deve ser .rtf")
    
    try:
        # Inicializa COM
        pythoncom.CoInitialize()
        
        # Cria instância do Word
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False  # Executa em background
        
        try:
            # Abre o documento RTF
            doc = word.Documents.Open(input_path)
            
            # Exporta para PDF
            doc.ExportAsFixedFormat(
                OutputFileName=output_path,
                ExportFormat=17,  # 17 = PDF
                OpenAfterExport=False
            )
            
            doc.Close(False)
            
        finally:
            word.Quit()
            pythoncom.CoUninitialize()
            
        if not os.path.exists(output_path):
            raise Exception("A conversão falhou - arquivo PDF não foi criado")
            
    except Exception as e:
        raise Exception(f"Falha na conversão RTF para PDF: {str(e)}")

# Versão alternativa se Word não estiver disponível
def rtf_to_pdf_fallback(input_path: str, output_path: str) -> None:
    """Método alternativo se o Word não estiver instalado"""
    try:
        from comtypes import client  # comtypes é mais leve que pywin32
        word = client.CreateObject("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(input_path)
        doc.SaveAs(output_path, FileFormat=17)  # 17 = PDF
        doc.Close()
        word.Quit()
    except Exception as e:
        raise Exception(f"Fallback também falhou: {str(e)}. Instale o Microsoft Word")