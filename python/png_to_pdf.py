from PIL import Image
import os

def png_to_pdf(input_path, output_path=None):
    try:
        image = Image.open(input_path).convert("RGB")
        if not output_path:
            base = os.path.splitext(input_path)[0]
            output_path = base + ".pdf"
        image.save(output_path, "PDF")
        return True, f"Arquivo salvo em: {output_path}"
    except Exception as e:
        return False, f"Erro ao converter PNG para PDF: {str(e)}"
