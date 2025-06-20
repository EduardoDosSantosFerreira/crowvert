from PIL import Image
import os

def png_to_ico(input_path, output_path):
    image = Image.open(input_path).convert("RGBA")
    # Você pode especificar tamanhos aqui (16x16, 32x32, 48x48, etc.)
    image.save(output_path, format="ICO", sizes=[(64, 64)])