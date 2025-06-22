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
| Rama Owarianto Putra Suharjito | 5027231049 |
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

*   **Hashing**
*   **Upload**
*   **Download**


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
  - Coordinator & Dokumentasi : Nisrina Atiqah Dwiputri Ridzki
