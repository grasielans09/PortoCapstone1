# PortoCapstone1
Additional Portfolio Capstone Project Module 1 Purwadhika JCDS-2604 Class
# Sistem Manajemen Nilai Siswa

Program ini merupakan aplikasi berbasis terminal untuk mengelola data siswa dan nilai di sebuah institusi pendidikan. Aplikasi ini memiliki tiga jenis pengguna dengan hak akses yang berbeda: **Admin**, **Teacher**, dan **Siswa**.

## Fitur Utama

1. **Login dan Hak Akses**
   - Terdapat tiga jenis pengguna: **Admin**, **Teacher**, dan **Siswa**.
   - Admin dan Teacher memiliki akses untuk mengelola data siswa dan nilai, sementara siswa hanya bisa melihat nilai mereka.

2. **Admin Menu**
   - **List Daftar Siswa**: Menampilkan seluruh data siswa.
   - **Input Data Siswa**: Menambahkan data siswa baru.
   - **Edit Data Siswa**: Mengubah informasi siswa yang ada.
   - **Hapus Data Siswa**: Menghapus data siswa.

3. **Teacher Menu**
   - **List Data Nilai**: Menampilkan data nilai seluruh siswa.
   - **Input Nilai**: Memasukkan nilai tugas, kuis, UTS, dan UAS untuk setiap siswa.
   - **Edit Nilai**: Mengubah nilai siswa.

4. **Siswa Menu**
   - **Laporan Nilai**: Siswa dapat melihat nilai mereka dan status kelulusan berdasarkan nilai akhir.

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama yang digunakan.
- **PrettyTable**: Digunakan untuk menampilkan data dalam format tabel.
- **Colorama**: Digunakan untuk memberikan warna pada teks di terminal.

## Cara Menggunakan Program

1. **Instalasi Dependensi**
   Pastikan Anda telah menginstal modul-modul berikut:
   ```bash
   pip install colorama prettytable

2. **Menjalankan Program Jalankan program dengan perintah:**
   ```bash
   python nama_file.py
3. **Login**
    Admin Login: Username: Admin, Password: admin123
    Teacher Login: Username: TeacherJCDS, Password: teacher123
    Siswa Login: Masukkan ID siswa yang terdaftar di sistem, misalnya 20241001.
4. **Navigasi Menu**
   Setelah login, setiap jenis pengguna akan diarahkan ke menu utama masing-masing. Setiap menu memiliki opsi yang dapat dipilih sesuai kebutuhan.

**Struktur Program**
- Login: Memastikan pengguna memiliki akses yang sesuai berdasarkan username dan password.
- Menu Admin: Mengelola data siswa (CRUD).
- Menu Teacher: Mengelola nilai siswa.
- Menu Siswa: Melihat laporan nilai dan status kelulusan.

**Contoh Data Siswa**
Berikut adalah beberapa data siswa yang sudah ada di database:
| ID Siswa  | Nama           | Kelas     | Alamat               |
|-----------|----------------|-----------|----------------------|
| 20241001  | Charlie Puth    | JCDS100   | Perum 3              |
| 20241002  | Shawn Mendes    | JCDS100   | Komplek Palem Raya   |
| 20241003  | Bernadya Ribka  | JCDS100   | Pesona Atlantis      |
| 20241004  | Taylor Swift    | JCDS100   | Serdang Asri 1       |


**Catatan**
- Pastikan untuk memasukkan nilai dalam rentang 0-100.
- Siswa dinyatakan Lulus jika nilai akhirnya lebih dari atau sama dengan 85.

**Pengembangan Selanjutnya**

Fitur tambahan yang bisa ditambahkan di masa depan:
- Pencarian data siswa berdasarkan nama.
- Export data siswa ke format CSV.
- Sistem autentikasi lebih aman dengan enkripsi password.
