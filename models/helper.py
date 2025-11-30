from db.database_question import connect_question
from db.database_diagnosis import connect_diagnosis
import mysql.connector

def load_questions_grouped():
    conn = connect_question()
    cur = conn.cursor()
    cur.execute("""
      SELECT c.id, c.name, q.id, q.question
      FROM categories c
      LEFT JOIN questions q ON q.category_id = c.id
      ORDER BY c.id, q.id
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    groups = {}
    for cat_id, cat_name, q_id, q_text in rows:
        if cat_id not in groups:
            groups[cat_id] = {"name": cat_name, "questions": []}
        if q_id:
            groups[cat_id]["questions"].append({"id": q_id, "text": q_text})
    return groups

def save_result(user_id, hasil_dict):
    conn = connect_diagnosis()
    cur = conn.cursor()
    saran = hasil_dict.get('saran', 'Perhatikan istirahat, olahraga ringan, konsultasi bila perlu.')
    cur.execute("""
        INSERT INTO results (user_id, stres, kecemasan, burnout, depresi, saran)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        user_id,
        hasil_dict.get('stres','-'),
        hasil_dict.get('kecemasan','-'),
        hasil_dict.get('burnout','-'),
        hasil_dict.get('depresi','-'),
        saran
    ))
    conn.commit()
    cur.close()
    conn.close()

def list_results_by_user(user_id):
    conn = connect_diagnosis()
    cur = conn.cursor()
    cur.execute("SELECT id, stres, kecemasan, burnout, depresi, saran, created_at FROM results WHERE user_id=%s ORDER BY created_at DESC", (user_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_all_results():
    # Note: cross-db join may require full db.table reference if privileges configured;
    # here we attempt to join with auth_db.users to show user name (works in default XAMPP)
    conn = connect_diagnosis()
    cur = conn.cursor()
    try:
        cur.execute("SELECT r.id, r.user_id, u.nama, r.stres, r.kecemasan, r.burnout, r.depresi, r.saran, r.created_at FROM results r LEFT JOIN auth_db.users u ON r.user_id = u.id ORDER BY r.created_at DESC")
        rows = cur.fetchall()
    except mysql.connector.Error:
        # fallback: if cross-db join not allowed, just pull results from diagnosis_db
        cur.execute("SELECT id, user_id, stres, kecemasan, burnout, depresi, saran, created_at FROM results ORDER BY created_at DESC")
        rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
