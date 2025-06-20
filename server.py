# server.py
import os
import hashlib
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

# --- Inisialisasi Aplikasi Flask ---
app = Flask(__name__)
FILES_DIR = "files_to_serve"
app.config["UPLOAD_FOLDER"] = FILES_DIR

# --- Konfigurasi Hash ---
# Perubahan: Tambahkan semua algoritma baru yang didukung hashlib
SUPPORTED_HASH_ALGORITHMS = [
    'sha256', 
    'sha512', 
    'sha1', 
    'md5', 
    'ripemd160', 
    'sha3_256', 
    'blake2b'
]

# --- Fungsi Helper ---
def calculate_hash(filepath, algorithm):
    """Menghitung hash dari file menggunakan algoritma yang ditentukan."""
    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        print(f"Peringatan: Algoritma '{algorithm}' tidak didukung oleh hashlib sistem ini.")
        return "N/A"
        
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hasher.update(byte_block)
    return hasher.hexdigest()

# --- Setup Awal ---
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

# --- Routing dan Endpoint API ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Tidak ada bagian file dalam request"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Tidak ada file yang dipilih"}), 400
    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return jsonify({"message": f"File '{filename}' berhasil diunggah."}), 201
    return jsonify({"error": "Terjadi kesalahan saat upload"}), 500

@app.route('/api/files/integrity')
def get_files_for_integrity_check():
    response_data = { "algorithms": SUPPORTED_HASH_ALGORITHMS, "files": [] }
    try:
        for filename in sorted(os.listdir(app.config["UPLOAD_FOLDER"])):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            if os.path.isfile(filepath):
                hashes = {algo: calculate_hash(filepath, algo) for algo in SUPPORTED_HASH_ALGORITHMS}
                response_data["files"].append({"filename": filename, "hashes": hashes})
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Menjalankan Server ---
if __name__ == '__main__':
    print(f"Menyajikan file dari: {os.path.abspath(app.config['UPLOAD_FOLDER'])}")
    print("Server berjalan di http://localhost:5000")
    app.run(debug=True, port=5000)