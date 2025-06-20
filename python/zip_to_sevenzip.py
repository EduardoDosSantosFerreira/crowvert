import py7zr
import zipfile
import os
import tempfile

def zip_to_sevenzip(zip_path, output_7z_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        with py7zr.SevenZipFile(output_7z_path, 'w') as archive:
            archive.writeall(temp_dir, arcname="")