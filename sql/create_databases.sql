-- DATABASE 1: auth_db
CREATE DATABASE IF NOT EXISTS auth_db;
USE auth_db;
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(150),
  email VARCHAR(150) UNIQUE,
  password VARCHAR(255),
  role ENUM('user','admin') DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DATABASE 2: question_db
CREATE DATABASE IF NOT EXISTS question_db;
USE question_db;
CREATE TABLE IF NOT EXISTS categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS questions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  category_id INT,
  question TEXT,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- contoh kategori & pertanyaan (opsional)
INSERT INTO categories (name) VALUES ('stres'), ('kecemasan'), ('burnout'), ('depresi');

-- tambahkan beberapa contoh pertanyaan (YA/TIDAK)
INSERT INTO questions (category_id, question) VALUES
(1, 'Apakah kamu merasa kewalahan setiap hari?'),
(1, 'Apakah pekerjaan/tugas terasa terlalu berat?'),
(1, 'Apakah kamu merasa sulit mengontrol emosi?'),
(1, 'Apakah kamu merasa tidak punya waktu istirahat?'),
(2, 'Apakah kamu sering overthinking?'),
(2, 'Apakah kamu merasa mudah panik?'),
(2, 'Apakah tubuhmu sering merasa berdebar?'),
(2, 'Apakah kamu gelisah saat mencoba tidur?'),
(3, 'Apakah kamu merasa lelah sepanjang hari?'),
(3, 'Apakah kamu kehilangan motivasi?'),
(3, 'Apakah kamu merasa jenuh dengan aktivitas harian?'),
(3, 'Apakah kamu mudah marah terhadap hal kecil?'),
(4, 'Apakah kamu merasa sedih tanpa alasan?'),
(4, 'Apakah kamu kehilangan minat terhadap hal yang dulu disukai?'),
(4, 'Apakah kamu merasa tidak berharga?');

-- DATABASE 3: diagnosis_db
CREATE DATABASE IF NOT EXISTS diagnosis_db;
USE diagnosis_db;
CREATE TABLE IF NOT EXISTS results (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  stres VARCHAR(50),
  kecemasan VARCHAR(50),
  burnout VARCHAR(50),
  depresi VARCHAR(50),
  saran TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
