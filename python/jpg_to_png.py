from PIL import Image
import os

def jpg_to_png(input_path, output_path):
    image = Image.open(input_path).convert("RGBA")
    image.save(output_path, "PNG")