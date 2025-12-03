# Mental Expert Web

Sistem Pakar Diagnosis Kesehatan Mental Berbasis Rule Engine

Status: Python 3.8+ | Flask 2.2.5 | MySQL 5.7+ | MIT License

---

## Daftar Isi

1. Deskripsi Singkat
2. Fitur Utama
3. Teknologi yang Digunakan
4. Persyaratan Sistem
5. Instalasi
6. Panduan Penggunaan
7. Struktur Project
8. Arsitektur Sistem
9. Rule Engine
10. Keamanan
11. Pengembangan Lebih Lanjut
12. Kontribusi
13. Lisensi

---

## Deskripsi Singkat

**Mental Expert Web** adalah aplikasi web berbasis Flask yang menggunakan teknologi **Artificial Intelligence (AI)** melalui **Expert System dengan Rule Engine** untuk mendiagnosis tingkat kesehatan mental pengguna.

Aplikasi ini dirancang untuk memberikan:

- Diagnosis awal tentang kesehatan mental
- Edukasi dan awareness tentang gangguan mental
- Rekomendasi penanganan yang dipersonalisasi
- Tracking riwayat diagnosis pengguna

Aplikasi ini dibangun sebagai **Tugas Akhir Semester (UAS)** untuk mata kuliah **Kecerdasan Buatan** dan mendemonstrasikan implementasi praktis dari expert system dalam aplikasi web.

---

## Fitur Utama

### Manajemen Pengguna

- Registrasi akun baru dengan validasi email
- Autentikasi login dengan enkripsi password (Werkzeug)
- Session management untuk keamanan
- Dashboard personal per pengguna

### Sistem Pakar (Expert System)

- **Rule Engine** dengan 7 rule utama untuk diagnosis
- Klasifikasi otomatis dari YA/TIDAK ke tingkat kesehatan (Rendah/Sedang/Tinggi)
- Multiple kombinasi rule untuk diagnosis yang lebih akurat
- Trigger rule berdasarkan kombinasi gejala kompleks

### Kuesioner Diagnosis

- 16 pertanyaan terstruktur dalam 4 kategori:
  - **Stres** (4 pertanyaan)
  - **Kecemasan** (4 pertanyaan)
  - **Burnout** (4 pertanyaan)
  - **Depresi** (4 pertanyaan)
- Interface yang user-friendly
- Instant processing dan hasil real-time

### Hasil dan Rekomendasi

- Skor per kategori (0-4)
- Klasifikasi tingkat kesehatan mental
- Kesimpulan dari rule engine yang aktif
- Rekomendasi personal berdasarkan rule
- Saran per-kategori sebagai fallback

### Riwayat Diagnosis

- Menyimpan semua hasil diagnosis pengguna
- Tracking progress kesehatan mental
- Timeline diagnosis dengan tanggal dan waktu
- Akses ke detail diagnosis sebelumnya

### Admin Panel

- Dashboard admin untuk melihat semua data pengguna
- Statistik dan laporan diagnosis pengguna
- Manajemen data users
- (Pengembangan lebih lanjut: export, filter, analytics)

---

## Teknologi yang Digunakan

| Komponen                  | Teknologi               | Versi            |
| ------------------------- | ----------------------- | ---------------- |
| **Backend Framework**     | Flask                   | 2.2.5            |
| **Database**              | MySQL                   | 5.7+             |
| **Database Driver**       | mysql-connector-python  | 8.1.0            |
| **Authentication**        | Flask-Login             | 0.6.2            |
| **Password Hashing**      | Werkzeug                | 2.2.3            |
| **PDF Generation**        | ReportLab               | 4.0.0            |
| **Environment Variables** | python-dotenv           | 1.0.0            |
| **Frontend**              | HTML5, CSS3, JavaScript |                  |
| **Templating Engine**     | Jinja2                  | (Built-in Flask) |
| **Programming Language**  | Python                  | 3.8+             |

---

## Persyaratan Sistem

### Perangkat Keras Minimum

- Prosesor: Intel i3 atau setara
- RAM: 2 GB
- Storage: 500 MB (untuk project + database)

### Perangkat Lunak

| Software         | Versi Minimum            | Catatan                                             |
| ---------------- | ------------------------ | --------------------------------------------------- |
| **Python**       | 3.8+                     | Download dari [python.org](https://www.python.org/) |
| **MySQL Server** | 5.7+                     | atau MariaDB 10.3+                                  |
| **Git**          | 2.0+                     | Untuk clone repository                              |
| **Browser**      | Versi terbaru            | Chrome, Firefox, Safari, Edge                       |
| **OS**           | Windows 7+, macOS, Linux | Cross-platform support                              |

---

## Instalasi

### Langkah 1: Persiapan (Windows PowerShell)

1. **Install Python** (jika belum)

   - Download dari https://www.python.org/downloads/
   - Pastikan centang "Add Python to PATH"

2. **Install MySQL Server** (jika belum)

   - Download MySQL Community Server dari https://dev.mysql.com/downloads/mysql/
   - Jalankan installer dan ikuti wizard setup

3. **Verifikasi instalasi:**
   ```powershell
   python --version
   mysql --version
   ```

### Langkah 2: Clone Repository

```powershell
cd "c:\Disc D\Kuliah\Kuliah Semester 3\Kecerdasan Buatan\UAS"
git clone https://github.com/fahrel-handsome/mental-expert-web.git
cd mental-expert-web
```

### Langkah 3: Setup Virtual Environment

```powershell
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\Activate.ps1
```

**Jika ada error permission denied:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Langkah 4: Install Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

**Dependencies yang akan diinstall:**

- Flask==2.2.5
- mysql-connector-python==8.1.0
- Flask-Login==0.6.2
- Werkzeug==2.2.3
- reportlab==4.0.0
- python-dotenv==1.0.0

### Langkah 5: Setup Database

**Opsi A: Menggunakan MySQL Command Line**

```powershell
mysql -u root -p < sql/create_databases.sql
```

Masukkan password MySQL Anda saat diminta.

**Opsi B: Menggunakan MySQL Workbench**

1. Buka MySQL Workbench
2. File → Run SQL Script
3. Pilih file `sql/create_databases.sql`
4. Klik Run

**Opsi C: Import Manual**

1. Buka MySQL Command Line Client atau Workbench
2. Copy-paste isi dari `sql/create_databases.sql`
3. Execute

### Langkah 6: Konfigurasi Environment

Buat file `.env` di root folder project:

```
# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASS=
SECRET_KEY=your-secret-key-here-ganti-dengan-string-random
```

**Catatan:**

- Ganti `DB_PASS` dengan password MySQL Anda (jika ada)
- Ganti `SECRET_KEY` dengan string random yang panjang untuk keamanan

### Langkah 7: Jalankan Aplikasi

```powershell
python app.py
```

**Output yang diharapkan:**

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
 * Press CTRL+C to quit
```

### Langkah 8: Akses Aplikasi

Buka browser dan kunjungi: **`http://127.0.0.1:5000/`**

---

## Panduan Penggunaan

### Alur User Reguler

#### 1. Registrasi Akun

```
Home → Daftar
├─ Input: Nama, Email, Password
├─ Validasi: Email unik, Password min 8 karakter
└─ Sukses → Redirect ke Login
```

**Screenshot-like Flow:**

```
┌─────────────────────────────┐
│  HALAMAN REGISTRASI         │
├─────────────────────────────┤
│ Nama:      [________________]│
│ Email:     [________________]│
│ Password:  [________________]│
│ [✓ DAFTAR] [KEMBALI]       │
└─────────────────────────────┘
```

#### 2. Login ke Sistem

```
Login → Input Email & Password
├─ Validasi Credential
├─ Sukses → Session di-set
└─ Redirect → Dashboard User
```

#### 3. Dashboard User

```
Dashboard User
├─ Ucapan Selamat Datang
├─ [Mulai Diagnosis Baru]
└─ Riwayat Diagnosis (Tabel)
   ├─ Tanggal
   ├─ Hasil (Stres, Kecemasan, Burnout, Depresi)
   ├─ Kesimpulan
   └─ [Lihat Detail]
```

#### 4. Kuesioner Diagnosis (Fitur Utama)

```
Mulai Diagnosis → Kuesioner (16 Pertanyaan)
├─ Kategori 1: Stres (4 pertanyaan)
├─ Kategori 2: Kecemasan (4 pertanyaan)
├─ Kategori 3: Burnout (4 pertanyaan)
├─ Kategori 4: Depresi (4 pertanyaan)
│
├─ Jawab setiap: YA / TIDAK
│  (Scoring: YA=+1, TIDAK=0)
│
└─ [PROSES HASIL]
   ↓
   RULE ENGINE BEKERJA
   ↓
   Tampilkan Hasil
```

**Format Pertanyaan:**

```
Kategori: STRES
─────────────────
[✓] Ya  [ ] Tidak  - Apakah kamu merasa kewalahan setiap hari?
[✓] Ya  [ ] Tidak  - Apakah pekerjaan/tugas terasa terlalu berat?
[ ] Ya  [✓] Tidak  - Apakah kamu merasa sulit mengontrol emosi?
[ ] Ya  [✓] Tidak  - Apakah kamu merasa tidak punya waktu istirahat?

Skor Stres: 2/4 → Klasifikasi: SEDANG
```

#### 5. Halaman Hasil Diagnosis

```
HASIL DIAGNOSIS ANDA
═════════════════════

Skor Per Kategori:
├─ Stres:      2/4 → SEDANG
├─ Kecemasan:  3/4 → SEDANG
├─ Burnout:    1/4 → RENDAH
└─ Depresi:    0/4 → RENDAH

Rule yang Tertrigger: R6
Kesimpulan: Beberapa kategori Anda berada pada tingkat sedang.

Rekomendasi Utama:
└─ Cobalah teknik relaksasi rutin, olahraga ringan,
   dan manajemen waktu.

Rekomendasi Per Kategori:
├─ Stres: Cobalah teknik relaksasi seperti pernapasan
│         dalam atau olahraga ringan.
├─ Kecemasan: Latih mindfulness, atur pola napas, dan
│            kurangi kafein.
├─ Burnout: Luangkan waktu untuk istirahat, hindari
│          multitasking, dan lakukan kegiatan menyenangkan.
└─ Depresi: Tetap lakukan aktivitas positif dan jaga
           hubungan sosial.

[← KEMBALI KE DASHBOARD] [DIAGNOSIS ULANG]
```

#### 6. Riwayat Diagnosis

```
Dashboard User → Riwayat Diagnosis
├─ [Diagnosis #1] 01/12/2024 → Stres:Sedang, ...
├─ [Diagnosis #2] 30/11/2024 → Stres:Rendah, ...
└─ [Diagnosis #3] 25/11/2024 → Stres:Tinggi, ...

[Lihat Detail] → Tampilkan hasil lengkap dari diagnosis tersebut
```

### Alur Admin

```
Halaman Admin (/admin)
├─ Statistik Pengguna
│  └─ Total Users: X, Total Diagnosis: Y
│
├─ Tabel Semua Diagnosis
│  ├─ User ID, Nama, Email
│  ├─ Hasil Diagnosis (Stres, Kecemasan, Burnout, Depresi)
│  └─ Tanggal Diagnosis
│
└─ Aksi Admin
   └─ (Pengembangan: Export, Delete, Edit, dll)
```

---

## Struktur Project

```
mental-expert-web/
│
├── app.py                      (Flask main application & routes)
├── config.py                   (Database & app configuration)
├── requirements.txt            (Python dependencies)
├── README.md                   (Dokumentasi ini)
├── LAPORAN_UAS.md             (Laporan tugas akhir semester)
├── .env.example                (Template environment variables)
│
├── admin/                      (Admin dashboard routes)
│   ├── __init__.py
│   └── admin_routes.py        (Admin blueprint & routes)
│
├── auth/                       (Authentication module)
│   ├── __init__.py
│   └── auth.py                (Register & login logic)
│
├── db/                         (Database connections)
│   ├── __init__.py
│   ├── database_auth.py       (Connection ke auth_db)
│   ├── database_diagnosis.py  (Connection ke diagnosis_db)
│   └── database_question.py   (Connection ke question_db)
│
├── models/                     (Business logic)
│   ├── __init__.py
│   └── helper.py              (Fungsi helper & queries)
│
├── sql/                        (Database schema)
│   └── create_databases.sql   (SQL untuk buat 3 database)
│
├── static/                     (Static files)
│   ├── css/
│   │   └── style.css          (Styling aplikasi)
│   └── js/
│       └── main.js            (JavaScript functions)
│
├── templates/                  (Jinja2 templates HTML)
│   ├── layout.html            (Base template)
│   ├── index.html             (Landing page)
│   ├── login.html             (Form login)
│   ├── register.html          (Form registrasi)
│   ├── questionnaire.html     (Kuesioner diagnosis)
│   ├── results.html           (Halaman hasil diagnosis)
│   ├── user_dashboard.html    (Dashboard user)
│   └── admin_dashboard.html   (Dashboard admin)
│
└── __pycache__/               (Python cache auto-generated)
```

---

## Arsitektur Sistem

### Arsitektur Umum (Layers)

```
┌─────────────────────────────────────────────┐
│         FRONTEND LAYER                      │
│    HTML/CSS/JavaScript + Jinja2             │
│  (Templates untuk UI/UX)                    │
└────────────────┬────────────────────────────┘
                 │ HTTP Requests/Responses
┌────────────────▼────────────────────────────┐
│      APPLICATION LAYER (Flask)              │
│  - Routes (@app.route)                      │
│  - Session Management                       │
│  - Request Handling                         │
│  - Blueprint Registration                   │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│     BUSINESS LOGIC LAYER                    │
│  - Rule Engine (Expert System AI)           │
│  - Score Calculation & Classification       │
│  - Authentication Logic                     │
│  - Helper Functions                         │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│      DATA ACCESS LAYER                      │
│  - Database Connections                     │
│  - Query Execution                          │
│  - Data Validation                          │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│      DATABASE LAYER (MySQL)                 │
│  - auth_db (Users)                          │
│  - question_db (Q&A)                        │
│  - diagnosis_db (Results)                   │
└──────────────────────────────────────────────┘
```

### Flow Aplikasi

```
START
  │
  ├─ User visit http://127.0.0.1:5000/
  │
  ├─ [Landing Page]
  │  ├─ Belum login? → Register / Login
  │  └─ Sudah login? → Dashboard
  │
  ├─ [Register Route] (/register)
  │  ├─ Input: nama, email, password
  │  ├─ Validasi & Hash password (Werkzeug)
  │  ├─ Simpan ke auth_db.users
  │  └─ Redirect → Login
  │
  ├─ [Login Route] (/login)
  │  ├─ Input: email, password
  │  ├─ Verifikasi di auth_db.users
  │  ├─ Set session[user_id, user_name, role]
  │  └─ Redirect → Dashboard
  │
  ├─ [Dashboard User] (/user)
  │  ├─ Tampilkan riwayat diagnosis
  │  ├─ Button "Mulai Diagnosis"
  │  └─ Button "Lihat Detail"
  │
  ├─ [Kuesioner] (/questionnaire - GET)
  │  ├─ Load 16 pertanyaan dari question_db
  │  └─ Tampilkan form YA/TIDAK
  │
  ├─ [Process Kuesioner] (/questionnaire - POST)
  │  ├─ Hitung skor: Stres, Kecemasan, Burnout, Depresi
  │  ├─ Klasifikasi: Rendah (0-1), Sedang (2-3), Tinggi (4)
  │  │
  │  ├─ *** RULE ENGINE DIJALANKAN ***
  │  ├─ Cek rule R1-R7
  │  ├─ Tentukan: kesimpulan + saran_utama + rule_aktif
  │  │
  │  ├─ Generate saran per kategori (fallback)
  │  ├─ Simpan ke diagnosis_db.results
  │  └─ Return hasil ke template
  │
  ├─ [Hasil Diagnosis] (/questionnaire - RESPONSE)
  │  ├─ Tampilkan skor per kategori
  │  ├─ Tampilkan klasifikasi
  │  ├─ Tampilkan kesimpulan (dari rule engine)
  │  ├─ Tampilkan rekomendasi utama
  │  └─ Tampilkan rekomendasi per kategori
  │
  └─ END

ADMIN FLOW:
  login → set role='admin' → redirect /admin
  /admin → tampilkan dashboard admin (tabel users, diagnosis)
```

---

## Rule Engine

Rule Engine adalah jantung dari expert system kami. Berikut 7 rule utama:

| Rule   | Kondisi                                                                    | Output                                       | Rekomendasi                                                        |
| ------ | -------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| **R1** | Stres=Tinggi AND Burnout=Tinggi                                            | Stres dan burnout sangat tinggi              | Kurangi beban kerja, istirahat panjang, konsultasi profesional     |
| **R2** | Depresi=Tinggi AND Kecemasan=Tinggi                                        | Depresi berat + kecemasan berat              | Segera konsultasi psikolog/psikiater                               |
| **R3** | Depresi=Tinggi AND Stres=Tinggi                                            | Depresi dan stres tinggi                     | Prioritaskan kesehatan mental, cari bantuan profesional            |
| **R4** | (Stres=Sedang AND Kecemasan=Tinggi) OR (Stres=Tinggi AND Kecemasan=Sedang) | Gangguan signifikan pada stres dan kecemasan | Teknik relaksasi intensif, kurangi beban, sesi konseling           |
| **R5** | Semua kategori=Rendah                                                      | Kondisi mental stabil                        | Pertahankan kebiasaan sehat, olahraga, aktivitas positif           |
| **R6** | 2+ kategori=Sedang                                                         | Beberapa kategori sedang                     | Teknik relaksasi rutin, olahraga ringan, manajemen waktu           |
| **R7** | 1 kategori=Tinggi                                                          | [Kategori] tinggi                            | Fokus pada perbaikan [kategori], pertimbangkan bantuan profesional |

### Scoring dan Klasifikasi

```
Setiap kategori ada 4 pertanyaan (YA/TIDAK):
├─ YA = +1 poin
└─ TIDAK = 0 poin

Total skor per kategori: 0-4

Klasifikasi:
├─ 0-1 poin → RENDAH (Alert: Normal)
├─ 2-3 poin → SEDANG (Alert: Perhatian)
└─ 4 poin   → TINGGI (Alert: Kritis)
```

### Contoh Eksekusi Rule Engine

```python
# Input dari kuesioner:
results = {
    'stres': 'Tinggi',      # Skor 4/4
    'kecemasan': 'Sedang',  # Skor 3/4
    'burnout': 'Tinggi',    # Skor 3/4
    'depresi': 'Rendah'     # Skor 0/4
}

# Rule Engine logic:
if stres == "Tinggi" and burnout == "Tinggi":  # R1
    rule_triggered = "R1"
    kesimpulan = "Tingkat stres dan burnout Anda sangat tinggi."
    saran = "Kurangi beban kerja, ambil waktu istirahat panjang, ..."
    return kesimpulan, saran, rule_triggered  # ← Output

# Output:
# Rule yang triggered: R1
# Kesimpulan: "Tingkat stres dan burnout Anda sangat tinggi."
# Saran: "Kurangi beban kerja, ambil waktu istirahat panjang, ..."
```

---

## Struktur Database

### Database 1: auth_db

Tabel: users

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(150),
  email VARCHAR(150) UNIQUE,
  password VARCHAR(255),           -- Hash with Werkzeug
  role ENUM('user','admin') DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Database 2: question_db

Tabel: categories

```sql
CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)                -- stres, kecemasan, burnout, depresi
);
```

Tabel: questions

```sql
CREATE TABLE questions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  category_id INT,
  question TEXT,
  FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

### Database 3: diagnosis_db

Tabel: results

```sql
CREATE TABLE results (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  stres VARCHAR(50),               -- Rendah, Sedang, Tinggi
  kecemasan VARCHAR(50),           -- Rendah, Sedang, Tinggi
  burnout VARCHAR(50),             -- Rendah, Sedang, Tinggi
  depresi VARCHAR(50),             -- Rendah, Sedang, Tinggi
  saran TEXT,                      -- Rekomendasi dari rule engine
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Keamanan

### Implementasi Keamanan

- Password Hashing: Menggunakan Werkzeug untuk hash password
- Session Management: Flask session dengan SECRET_KEY yang aman
- SQL Injection Prevention: Menggunakan parameterized queries
- CSRF Protection: Recommended untuk pengembangan lebih lanjut
- Input Validation: Validasi di server-side

### Rekomendasi Keamanan Produksi

```python
# .env file (JANGAN commit ke GitHub!)
DB_HOST=localhost
DB_USER=root
DB_PASS=your-secure-password
SECRET_KEY=generate-random-string-panjang-minimal-32-char

# Deployment:
- Gunakan HTTPS/SSL certificate
- Set Flask DEBUG=False
- Gunakan production WSGI server (Gunicorn, uWSGI)
- Implement CORS jika perlu API external
- Rate limiting untuk prevent brute force
```

---

## Testing

### Manual Testing Checklist

- Registrasi akun baru
- Login dengan email dan password
- Logout dari aplikasi
- Akses dashboard user (hanya saat login)
- Mulai diagnosis (16 pertanyaan)
- Submit kuesioner
- Lihat hasil diagnosis
- Lihat riwayat diagnosis
- Admin login dan akses /admin
- Verify database entries

### Contoh Unit Test untuk Pengembangan

```bash
# Install pytest
pip install pytest

# Jalankan test
pytest tests/ -v
```

---

## Pengembangan Lebih Lanjut

### Fitur yang Direncanakan

1. **Export PDF**: Download hasil diagnosis sebagai PDF
2. **Reset Password**: Email verification untuk reset password
3. **Machine Learning**: Upgrade dari rule engine ke neural network
4. **Mobile App**: Flutter/React Native untuk mobile version
5. **Chatbot AI**: Konsultasi awal dengan chatbot
6. **Email Notifications**: Reminder diagnosis berkala
7. **Advanced Analytics**: Dashboard trend kesehatan mental populasi
8. **User Profile**: Edit profil, foto, preferensi
9. **Multi-language**: Support bahasa Inggris dan bahasa lain
10. **Appointment Booking**: Booking konsultasi dengan profesional

### Known Issues dan TODO

- UI/UX perlu improvement (design lebih modern)
- Belum ada email notification system
- Admin panel belum fully functional
- Belum ada unit test
- Database migration tool belum ada
- API endpoint belum ada (untuk mobile app)

---

## Kontribusi

Jika ingin berkontribusi pada project ini:

1. Fork repository

   ```bash
   Buka https://github.com/fahrel-handsome/mental-expert-web
   Klik tombol "Fork"
   ```

2. Clone fork Anda

   ```bash
   git clone https://github.com/YOUR_USERNAME/mental-expert-web.git
   cd mental-expert-web
   ```

3. Buat branch baru

   ```bash
   git checkout -b feature/nama-fitur
   ```

4. Commit perubahan

   ```bash
   git add .
   git commit -m "feat: Deskripsi fitur baru"
   ```

5. Push ke fork Anda

   ```bash
   git push origin feature/nama-fitur
   ```

6. Buat Pull Request
   - Buka GitHub
   - Klik "Pull Request"
   - Isi deskripsi perubahan
   - Klik "Create Pull Request"

---

## Lisensi

Project ini dilisensikan di bawah **MIT License**. Lihat file `LICENSE` untuk detail lebih lanjut.

---

## Kontak dan Support

- **Author**: Fahrel Handsome
- **Repository**: https://github.com/fahrel-handsome/mental-expert-web
- **Issues**: https://github.com/fahrel-handsome/mental-expert-web/issues
- **Email**: [Hubungi melalui GitHub]

---

## Disclaimer

Mental Expert Web adalah aplikasi untuk tujuan edukasi dan deteksi dini kesehatan mental.

Perlu diketahui: Aplikasi ini BUKAN pengganti untuk konsultasi dengan profesional kesehatan mental yang bersertifikat.

Jika Anda mengalami gejala kesehatan mental yang serius, segera konsultasikan dengan:

- Psikolog
- Psikiater
- Dokter spesialis
- Layanan crisis hotline

---

## Referensi dan Sumber Bacaan

1. Russell, S. J., & Norvig, P. (2020). _Artificial Intelligence: A Modern Approach_.
2. Negnevitsky, M. (2011). _Expert Systems: Principles and Practice_.
3. Flask Official Documentation: https://flask.palletsprojects.com/
4. MySQL Official Documentation: https://dev.mysql.com/doc/
5. World Health Organization - Mental Health: https://www.who.int/news-room/fact-sheets/detail/mental-health
6. Anxiety and Depression Association: https://adaa.org/

---

## Catatan Akademik

**Tugas Akhir Semester (UAS)**

- **Mata Kuliah**: Kecerdasan Buatan
- **Semester**: 3
- **Tahun Akademik**: 2024/2025
- **Universitas**: [Universitas Anda]
- **Program Studi**: [Program Studi Anda]

Laporan lengkap dapat dilihat di file `LAPORAN_UAS.md`.

---

---

Terima kasih telah menggunakan Mental Expert Web.

Jika aplikasi ini membantu Anda, silakan star repository ini di GitHub.

Last Updated: Desember 2024
