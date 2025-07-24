import os
import py7zr
import zipfile
def sevenzip_to_zip(input_path, output_path):
    temp_dir = input_path + "_temp_extracted"
    try:
        with py7zr.SevenZipFile(input_path, mode='r') as archive:
            archive.extractall(path=temp_dir)
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, temp_dir)
                    zipf.write(full_path, rel_path)
    finally:
        import shutil
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)