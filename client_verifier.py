# client_verifier.py
import os
import requests

# --- KONFIGURASI ---
SERVER_URL = "http://localhost:5000"

# --- FUNGSI UTAMA ---
def run_integrity_checker_cli():
    print("\n" + "="*40)
    print("    CRYPTO TOOLKIT - FILE INTEGRITY    ")
    print("="*40)
    try:
        response = requests.get(f"{SERVER_URL}/api/files/integrity")
        response.raise_for_status()
        data = response.json()
        available_files = data.get('files', [])
        
        if not available_files:
            print("\nTidak ada file di server.")
            return

        print("\nFile yang ada di Server:")
        for i, f in enumerate(available_files):
            print(f"  {i+1}. {f['filename']}")
        
        file_choice_str = input("\nPilih nomor file untuk dilihat detail hash-nya: ")
        file_choice = int(file_choice_str) - 1
        
        if not (0 <= file_choice < len(available_files)):
            print("Pilihan tidak valid.")
            return
            
        file_info = available_files[file_choice]
        
        print(f"\nHash untuk file: {file_info['filename']}")
        for algo, hash_val in file_info['hashes'].items():
            print(f"  {algo.upper()}: {hash_val}")

    except (ValueError, IndexError):
        print("Input tidak valid. Harap masukkan nomor.")
    except requests.exceptions.RequestException as e:
        print(f"\nError: Tidak dapat terhubung ke server di {SERVER_URL}.")
        print(f"Detail: {e}")
    except Exception as e:
        print(f"Terjadi error yang tidak terduga: {e}")

# --- Menjalankan skrip ---
if __name__ == '__main__':
    run_integrity_checker_cli()