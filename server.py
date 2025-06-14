# server.py
import os
import hashlib
from flask import Flask, jsonify, send_from_directory, abort, render_template # Tambahkan render_template

app = Flask(__name__) # __name__ penting untuk path template dan static
FILES_DIR = "files_to_serve"
# Path absolut untuk direktori files_to_serve
app.config["FILES_DIR"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILES_DIR)


# Pastikan direktori files_to_serve ada
if not os.path.exists(app.config["FILES_DIR"]):
    os.makedirs(app.config["FILES_DIR"])
    with open(os.path.join(app.config["FILES_DIR"], "sample.txt"), "w") as f:
        f.write("Ini adalah konten file contoh untuk demonstrasi integritas.")
    print(f"Direktori '{FILES_DIR}' dibuat. Silakan tambahkan file di sana.")

# Fungsi calculate_sha256 tetap sama

def calculate_sha256(filepath):
    """Menghitung hash SHA-256 dari sebuah file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Endpoint baru untuk menyajikan frontend HTML
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') # Akan mencari index.html di folder 'templates'

@app.route('/files', methods=['GET'])
def list_files():
    """Endpoint untuk menampilkan daftar file dan hash SHA-256 mereka."""
    files_info = []
    try:
        for filename in os.listdir(app.config["FILES_DIR"]):
            filepath = os.path.join(app.config["FILES_DIR"], filename)
            if os.path.isfile(filepath):
                file_hash = calculate_sha256(filepath)
                files_info.append({"filename": filename, "sha256_hash": file_hash})
        return jsonify(files_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    """Endpoint untuk mengunduh file."""
    try:
        return send_from_directory(app.config["FILES_DIR"], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, description="File not found")

@app.route('/hash/<filename>', methods=['GET'])
def get_file_hash(filename):
    """Endpoint untuk mendapatkan hash SHA-256 dari file tertentu."""
    filepath = os.path.join(app.config["FILES_DIR"], filename)
    if os.path.isfile(filepath):
        file_hash = calculate_sha256(filepath)
        return jsonify({"filename": filename, "sha256_hash": file_hash})
    else:
        abort(404, description="File not found")

if __name__ == '__main__':
    print(f"Menyajikan file dari direktori: {app.config['FILES_DIR']}")
    print("Frontend tersedia di http://localhost:5000/")
    app.run(debug=True, port=5000)
