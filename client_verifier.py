# client_verifier.py
import os
import hashlib
import requests

SERVER_URL = "http://localhost:5000"
DOWNLOAD_DIR = "downloaded_files"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def calculate_sha256_local(filepath):
    """Menghitung hash SHA-256 dari file lokal."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def verify_file_integrity():
    # 1. Dapatkan daftar file dari server
    try:
        response_files = requests.get(f"{SERVER_URL}/files")
        response_files.raise_for_status() # Cek jika ada error HTTP
        available_files = response_files.json()
        if not available_files:
            print("Tidak ada file tersedia di server.")
            return
        
        print("File yang tersedia di server:")
        for i, file_info in enumerate(available_files):
            print(f"{i+1}. {file_info['filename']}")
        
        choice = input(f"Masukkan nomor file yang ingin diunduh (1-{len(available_files)}): ")
        try:
            selected_index = int(choice) - 1
            if not (0 <= selected_index < len(available_files)):
                raise ValueError
            filename_to_download = available_files[selected_index]['filename']
            expected_hash_from_server = available_files[selected_index]['sha256_hash']
        except ValueError:
            print("Pilihan tidak valid.")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error saat menghubungi server untuk daftar file: {e}")
        # Jika tidak bisa dapat daftar file, minta input manual
        filename_to_download = input("Masukkan nama file yang ingin diunduh (misal: sample.txt): ")
                                                                                                [ Read 104 lines ]
