# FP-Kriptografi-Kelompok6
# File Integrity Checker (Python Flask & Vanilla JS)

## Anggota
| Nama Anggota        | NRP         |
|---------------------|-------------|
| Acintya Edria Sudarsono | 5027231020 |
| Dian Anggraeni | 5027231016 |
| Tsaldia Hukma Cita | 5027231036 |
| Rafika Az Zahra Kusumastuti | 5027231050 |
| Nisrina Atiqah Dwiputri Ridzki | 5027231075 |
| Riskiyatul Nur Oktarani | 5027231013 |
| Fikri Aulia | 5027231026 |
| Rama Owarianto Ganesh | 5027231049 |
| Muhammad Andrean Rizq Prasetio | 5027231052 |

Proyek ini mendemonstrasikan konsep fungsi hash dan verifikasi integritas file menggunakan backend Python Flask dan frontend Vanilla JavaScript. Pengguna dapat melihat daftar file yang tersedia di server, mengunduhnya, dan kemudian memverifikasi apakah file yang diunduh identik dengan file asli di server dengan membandingkan hash SHA-256 milik user.

## Daftar Isi

- [Fitur](#fitur)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Proyek](#struktur-proyek)
- [Cara Kerja](#cara-kerja)
  - [Backend (Flask Server)](#backend-flask-server)
  - [Frontend (HTML & JavaScript)](#frontend-html--javascript)
- [Instalasi dan Menjalankan](#instalasi-dan-menjalankan)
  - [Prasyarat](#prasyarat)
  - [Langkah-langkah Menjalankan](#langkah-langkah-menjalankan)
- [Penggunaan](#penggunaan)
- [Pembuktian Integritas](#pembuktian-integritas)
  - [Skenario 1: Verifikasi Berhasil](#skenario-1-verifikasi-berhasil)
  - [Skenario 2: Verifikasi Gagal (File Diubah)](#skenario-2-verifikasi-gagal-file-diubah)
- [Contributors](#contributors)

## Fitur

*   **Backend Server (Flask):**
    *   Menyajikan daftar file yang tersedia dari direktori `files_to_serve/`.
    *   Menghitung dan menyediakan hash SHA-256 untuk setiap file.
    *   Memungkinkan pengunduhan file.
    *   Menyediakan endpoint API untuk daftar file dan hash individual.
*   **Frontend (HTML, CSS, JavaScript):**
    *   Menampilkan daftar file dari server beserta hash SHA-256 mereka.
    *   Tombol untuk mengunduh file langsung dari browser.
    *   Fitur untuk memilih file lokal (yang telah diunduh) untuk verifikasi.
    *   Secara otomatis mengambil hash yang diharapkan dari server berdasarkan nama file yang dipilih.
    *   Menghitung hash SHA-256 file lokal di sisi klien menggunakan Web Crypto API.
    *   Membandingkan hash lokal dengan hash server dan menampilkan status verifikasi (berhasil/gagal).

## Teknologi yang Digunakan

*   **Backend:**
    *   Python 3
    *   Flask (Framework web mikro)
    *   `hashlib` (Modul Python standar untuk hashing)
*   **Frontend:**
    *   HTML5
    *   CSS3 (Styling dasar)
    *   Vanilla JavaScript (ES6+)
    *   Fetch API (Untuk komunikasi dengan backend)
    *   Web Crypto API (`crypto.subtle.digest`) (Untuk hashing di sisi klien)

 ## Struktur Proyek
 ![image](https://github.com/user-attachments/assets/afc8f884-d658-4d31-b47d-7e89ea9e313b)

 ## Cara Kerja

### Backend (Flask Server - `server.py`)

1.  **Inisialisasi**: Saat server dimulai, ia memeriksa keberadaan direktori `files_to_serve/`. Jika tidak ada, direktori tersebut akan dibuat beserta file `sample.txt` contoh.
2.  **Fungsi Hash**: `calculate_sha256(filepath)` digunakan untuk menghitung hash SHA-256 dari sebuah file dengan membacanya dalam _chunks_ agar efisien.
3.  **Endpoints API**:
    *   `/` (GET): Menyajikan halaman frontend `index.html`.
    *   `/files` (GET): Mengembalikan daftar JSON berisi nama file dan hash SHA-256 mereka dari direktori `files_to_serve/`.
    *   `/download/<filename>` (GET): Memungkinkan klien untuk mengunduh file tertentu dari direktori `files_to_serve/`.
    *   `/hash/<filename>` (GET): Mengembalikan JSON berisi nama file dan hash SHA-256 spesifik untuk file tersebut. Ini digunakan sebagai _fallback_ oleh frontend jika file tidak ada dalam cache daftar file awal.

### Frontend (HTML & JavaScript - `templates/index.html`)

1.  **Memuat Daftar File**: Saat halaman dimuat, fungsi `fetchFiles()` dipanggil. Fungsi ini:
    *   Mengambil daftar file dan hashnya dari endpoint `/files` server.
    *   Menyimpan daftar ini dalam `serverFilesCache` untuk penggunaan selanjutnya.
    *   Menampilkan daftar file dalam tabel HTML, lengkap dengan tombol "Download".
2.  **Mengunduh File**: Mengklik tombol "Download" akan mengarahkan browser untuk mengunduh file dari endpoint `/download/<filename>`.
3.  **Verifikasi File**:
    *   Pengguna memilih file dari komputer lokal mereka (biasanya file yang baru saja diunduh) menggunakan input `<input type="file">`.
    *   Ketika tombol "Verify Selected File" diklik, fungsi `verifyFile()` dijalankan:
        *   Nama file lokal yang dipilih diambil.
        *   Skrip mencoba menemukan hash yang sesuai untuk nama file tersebut dari `serverFilesCache`.
        *   Jika tidak ditemukan di cache, skrip akan mencoba mengambil hash langsung dari endpoint `/hash/<filename>` server.
        *   Jika hash server berhasil didapatkan, fungsi `calculateSHA256FromFile()` dipanggil. Fungsi ini menggunakan `crypto.subtle.digest` (Web Crypto API) untuk menghitung hash SHA-256 dari file lokal yang dipilih pengguna. Proses ini terjadi sepenuhnya di browser klien.
        *   Hash yang dihitung secara lokal kemudian dibandingkan dengan hash yang diharapkan dari server.
        *   Hasil perbandingan (berhasil atau gagal) ditampilkan kepada pengguna.

## Instalasi dan Menjalankan

### Prasyarat

*   Python 3.x
*   PIP (Python package installer)
*   Browser web modern yang mendukung Fetch API dan Web Crypto API (Chrome, Firefox, Edge, Safari terbaru).

### Langkah-langkah Menjalankan

1.  **Clone Repositori (GitHub):**

2.  **Install Dependensi (Flask):**
    ```bash
    pip install Flask
    ```

3.  **Siapkan File untuk Server:**
    *   Buat direktori `files_to_serve/` di root proyek jika belum ada.
    *   Tempatkan beberapa file contoh di dalam direktori `files_to_serve/` (misalnya, `sample.txt`, `image.jpg`, `document.pdf`). Server akan otomatis membuat `sample.txt` jika direktori kosong saat pertama kali dijalankan.

4.  **Jalankan Server Flask:**
    ```bash
    python server.py
    ```
    Server akan berjalan dan output dapat dilihat di terminal, termasuk URL tempat frontend tersedia (biasanya `http://localhost:5000/`).

5.  **Akses Frontend:**
    Buka browser web dan navigasikan ke `http://localhost:5000/`.

    ![image](https://github.com/user-attachments/assets/2b37a0fb-d5b1-47d5-b245-2c1b251e5c38)



## Penggunaan

1.  Halaman akan menampilkan daftar file yang ada di server beserta hash SHA-256.
2.  Klik tombol **"Download"** di samping file yang ingin dounduh.
3.  Di bagian **"Verify Downloaded File"**:
    *   Klik **"Choose File"** dan pilih file yang baru saja terunduh.
    *   Klik tombol **"Verify Selected File"**.
4.  Hasil verifikasi akan muncul, memberitahu apakah integritas file terjaga atau tidak.

## Pembuktian Integritas

Konsep utama di sini adalah jika hash SHA-256 dari file yang diunduh sama persis dengan hash SHA-256 dari file asli di server, maka file tersebut tidak berubah selama proses pengunduhan.

### Skenario 1: Verifikasi Berhasil

1.  Unduh file `sample.txt` dari server.
2.  Pilih file `sample.txt` yang baru diunduh untuk diverifikasi.
3.  Hasilnya akan menunjukkan **"[✓] VERIFICATION SUCCESSFUL: File integrity is intact."**
    ![image](https://github.com/user-attachments/assets/9c1588fe-ed38-4ef8-b769-943aee9b2988)



### Skenario 2: Verifikasi Gagal (File Diubah)

Untuk mendemonstrasikan kegagalan verifikasi:

1.  Unduh file `sample.txt` dari server. Lakukan verifikasi awal; hasilnya harus berhasil.
2.  **Ubah file yang telah diunduh**: Buka file `sample.txt` yang ada di direktori unduhan menggunakan editor teks. Tambahkan atau hapus satu karakter atau kata, lalu simpan file tersebut.
3.  Kembali ke halaman frontend.
4.  Di bagian "Verify Downloaded File", pilih kembali file `sample.txt` yang **sudah diubah**.
5.  Klik "Verify Selected File".
6.  Hasilnya akan menunjukkan **"[!] VERIFICATION FAILED: File may be corrupted or modified."** Ini karena hash dari file yang diubah tidak akan cocok lagi dengan hash asli dari server.
   ![image](https://github.com/user-attachments/assets/f35be052-286c-4e17-9117-9e82ee9a7a91)


Ini membuktikan bahwa perubahan pada file akan menghasilkan hash yang berbeda sehingga memungkinkan deteksi pemalsuan atau kerusakan data.

## Contributors
* Backend Development
  - Backend Lead & API Design : Acintya Edria Sudarsono
  - Backend Logic & Error Handling : Rama Owarianto P.S.
  - Backend Testing & Deployment Setup : Tsaldia Hukma Cita
* Frontend Development
  - Frontend Lead & HTML Structure : Riskiyatul Nur Oktarani
  - JavaScript Logic, core functionality : Fikri Aulia A
  - UI/UX & Styling : Muhammad Andrean Rizq Prasetio
  - Frontend testing & Usability : Dian Anggraeni Putri
* Dokumentasi & Manajemen
  - Technical Writer : Rafika Az Zahra Kusumastuti
  - Coordinator & Dokumentasi : 
