from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import SECRET_KEY
from auth.auth import register_user, verify_user
from models.helper import load_questions_grouped, save_result, list_results_by_user
from admin.admin_routes import admin_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(admin_bp)

# =====================================================================================
#  BAGIAN 1 — ADVICE PER KATEGORI (Fallback untuk saran jika rule tidak spesifik)
# =====================================================================================
ADVICE_MAP = {
    "stres": {
        "Rendah": "Pertahankan kebiasaan sehat dan tetap atur waktu dengan baik.",
        "Sedang": "Cobalah teknik relaksasi seperti pernapasan dalam atau olahraga ringan.",
        "Tinggi": "Lakukan istirahat cukup dan kurangi aktivitas berlebihan."
    },
    "kecemasan": {
        "Rendah": "Pertahankan kondisi emosional yang stabil dan tetap kelola stres dengan baik.",
        "Sedang": "Latih mindfulness, atur pola napas, dan kurangi kafein.",
        "Tinggi": "Pertimbangkan konsultasi profesional bila kecemasan mulai mengganggu aktivitas."
    },
    "burnout": {
        "Rendah": "Kondisi masih aman, tetap jaga pola kerja dan waktu istirahat.",
        "Sedang": "Luangkan waktu untuk istirahat, hindari multitasking, dan lakukan kegiatan menyenangkan.",
        "Tinggi": "Kurangi beban kerja atau ambil waktu istirahat lebih panjang, burnout sudah tinggi."
    },
    "depresi": {
        "Rendah": "Tetap lakukan aktivitas positif dan jaga hubungan sosial.",
        "Sedang": "Bangun rutinitas sehat dan bicarakan perasaan dengan orang yang dapat dipercaya.",
        "Tinggi": "Segera konsultasi dengan profesional karena gejala cukup berat."
    }
}

def generate_advices(results):
    """Fallback per kategori"""
    advices = []
    for kategori, level in results.items():
        kategori_key = kategori.lower()
        if kategori_key in ADVICE_MAP and level in ADVICE_MAP[kategori_key]:
            advices.append(f"{kategori_key.capitalize()}: {ADVICE_MAP[kategori_key][level]}")
    return advices

# =====================================================================================
#  BAGIAN 2 — RULE ENGINE (Sistem Pakar)
# =====================================================================================
def rule_engine(results):
    stres = results.get("stres")
    kec = results.get("kecemasan")
    burn = results.get("burnout")
    dep = results.get("depresi")

    rule_triggered = None
    kesimpulan = ""
    saran = ""

    # RULE 1 — Kombinasi Stres Tinggi + Burnout Tinggi
    if stres == "Tinggi" and burn == "Tinggi":
        rule_triggered = "R1"
        kesimpulan = "Tingkat stres dan burnout Anda sangat tinggi."
        saran = "Kurangi beban kerja, ambil waktu istirahat panjang, dan pertimbangkan konsultasi profesional."
        return kesimpulan, saran, rule_triggered

    # RULE 2 — Depresi Tinggi + Kecemasan Tinggi
    if dep == "Tinggi" and kec == "Tinggi":
        rule_triggered = "R2"
        kesimpulan = "Tanda depresi berat disertai kecemasan berat."
        saran = "Sangat disarankan untuk segera berkonsultasi dengan psikolog atau psikiater."
        return kesimpulan, saran, rule_triggered

    # RULE 3 — Depresi Tinggi + Stres Tinggi
    if dep == "Tinggi" and stres == "Tinggi":
        rule_triggered = "R3"
        kesimpulan = "Depresi dan stres berada pada tingkat tinggi."
        saran = "Prioritaskan kesehatan mental dan segera mencari bantuan profesional."
        return kesimpulan, saran, rule_triggered

    # RULE 4 — Kombinasi sedang+tinggi antara stres dan kecemasan
    if (stres == "Sedang" and kec == "Tinggi") or (stres == "Tinggi" and kec == "Sedang"):
        rule_triggered = "R4"
        kesimpulan = "Terdapat gangguan signifikan pada stres dan kecemasan."
        saran = "Lakukan teknik relaksasi intensif dan kurangi beban kerja. Pertimbangkan sesi konseling."
        return kesimpulan, saran, rule_triggered

    # RULE 5 — Semua kategori rendah
    if stres == kec == burn == dep == "Rendah":
        rule_triggered = "R5"
        kesimpulan = "Kondisi mental Anda stabil."
        saran = "Pertahankan kebiasaan sehat, olahraga, dan aktivitas positif."
        return kesimpulan, saran, rule_triggered

    # RULE 6 — Dua kategori sedang atau lebih
    medium_count = sum(1 for v in results.values() if v == "Sedang")
    if medium_count >= 2:
        rule_triggered = "R6"
        kesimpulan = "Beberapa kategori Anda berada pada tingkat sedang."
        saran = "Cobalah teknik relaksasi rutin, olahraga ringan, dan manajemen waktu."
        return kesimpulan, saran, rule_triggered

    # RULE 7 — Satu kategori tinggi
    high = [k for k, v in results.items() if v == "Tinggi"]
    if len(high) == 1:
        rule_triggered = "R7"
        kategori = high[0].capitalize()
        kesimpulan = f"{kategori} Anda berada pada tingkat tinggi."
        saran = f"Fokus pada perbaikan {kategori.lower()} dan pertimbangkan bantuan profesional jika keluhan menetap."
        return kesimpulan, saran, rule_triggered

    # Fallback jika tidak kena rule mana pun
    return "Kondisi umum terdeteksi.", "Ikuti saran per kategori untuk tindak lanjut.", "R0"

# =====================================================================================
#  Helper classify
# =====================================================================================
def classify(score):
    if score >= 4:
        return "Tinggi"
    elif score >= 2:
        return "Sedang"
    else:
        return "Rendah"

# =====================================================================================
#  ROUTING
# =====================================================================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        password = request.form['password']
        ok, err = register_user(nama, email, password)
        if ok:
            flash('Registrasi berhasil. Silakan login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Gagal registrasi: ' + str(err), 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pw = request.form['password']
        row = verify_user(email, pw)
        if row:
            session['user_id'] = row[0]
            session['user_name'] = row[1]
            session['role'] = row[2]
            flash('Login berhasil', 'success')
            if row[2] == 'admin':
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            flash('Email atau password salah', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/user')
def user_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    results = list_results_by_user(session['user_id'])
    return render_template('user_dashboard.html', name=session.get('user_name'), results=results)

# =====================================================================================
#  ROUTE QUESTIONNAIRE (UPDATE RULE ENGINE)
# =====================================================================================
@app.route('/questionnaire', methods=['GET','POST'])
def questionnaire():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    groups = load_questions_grouped()

    if request.method == 'POST':
        scores = {}
        results = {}

        # Hitung skor tiap kategori
        for cat_id, data in groups.items():
            cat_name = data['name'].lower()
            qs = data['questions']
            score = 0
            for q in qs:
                val = request.form.get(f"q_{q['id']}", 'tidak')
                if val == 'ya':
                    score += 1

            scores[cat_name] = score
            results[cat_name] = classify(score)

        # ===============================
        #     RULE ENGINE DIPANGGIL
        # ===============================
        kesimpulan, saran_utama, rule_aktif = rule_engine(results)

        # Saran biasa (per-kategori)
        advices = generate_advices(results)

        # Simpan data lengkap
        hasil_map = {
            'stres': results.get('stres'),
            'kecemasan': results.get('kecemasan'),
            'burnout': results.get('burnout'),
            'depresi': results.get('depresi'),
            'kesimpulan': kesimpulan,
            'saran_utama': saran_utama,
            'rule': rule_aktif
        }

        save_result(session['user_id'], hasil_map)

        return render_template(
            'results.html',
            results=hasil_map,
            raw_scores=scores,
            advices=advices
        )

    return render_template('questionnaire.html', groups=groups)

# =====================================================================================

if __name__ == '__main__':
    app.run(debug=True)
