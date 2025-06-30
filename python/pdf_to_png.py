from pdf2image import convert_from_path
import os

def pdf_to_png(input_path, output_folder):
    poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"
    images = convert_from_path(input_path, poppler_path=poppler_path)
    
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    for i, image in enumerate(images):
        output_file = os.path.join(output_folder, f"{base_name}_page_{i + 1}.png")
        image.save(output_file, "PNG")