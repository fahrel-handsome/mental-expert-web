from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db.database_question import connect_question
from models.helper import get_all_results

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# simple admin check
def is_admin():
    return session.get('role') == 'admin'

@admin_bp.route('/')
def index():
    if not is_admin():
        flash('Akses admin diperlukan', 'danger')
        return redirect(url_for('login'))
    # load categories & questions
    conn = connect_question()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM categories')
    cats = cur.fetchall()
    data = {}
    for c in cats:
        cur.execute('SELECT id, question FROM questions WHERE category_id=%s', (c[0],))
        qs = cur.fetchall()
        data[c[0]] = {'name': c[1], 'questions': qs}
    cur.close()
    conn.close()
    results = get_all_results()
    return render_template('admin_dashboard.html', data=data, results=results)

@admin_bp.route('/add_category', methods=['POST'])
def add_category():
    if not is_admin():
        flash('Akses admin', 'danger')
        return redirect(url_for('login'))
    name = request.form.get('category_name')
    if not name:
        flash('Nama kategori diperlukan', 'warning')
        return redirect(url_for('admin.index'))
    conn = connect_question()
    cur = conn.cursor()
    cur.execute('INSERT INTO categories (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close(); conn.close()
    flash('Kategori ditambahkan', 'success')
    return redirect(url_for('admin.index'))

@admin_bp.route('/add_question', methods=['POST'])
def add_question():
    if not is_admin():
        flash('Akses admin', 'danger')
        return redirect(url_for('login'))
    cat_id = request.form.get('category_id')
    qtext = request.form.get('question_text')
    if not cat_id or not qtext:
        flash('Kategori dan pertanyaan diperlukan', 'warning')
        return redirect(url_for('admin.index'))
    conn = connect_question(); cur = conn.cursor()
    cur.execute('INSERT INTO questions (category_id, question) VALUES (%s, %s)', (cat_id, qtext))
    conn.commit(); cur.close(); conn.close()
    flash('Pertanyaan ditambahkan', 'success')
    return redirect(url_for('admin.index'))

@admin_bp.route('/delete_question/<int:q_id>')
def delete_question(q_id):
    if not is_admin():
        flash('Akses admin', 'danger')
        return redirect(url_for('login'))
    conn = connect_question(); cur = conn.cursor()
    cur.execute('DELETE FROM questions WHERE id=%s', (q_id,))
    conn.commit(); cur.close(); conn.close()
    flash('Pertanyaan dihapus', 'success')
    return redirect(url_for('admin.index'))

@admin_bp.route('/delete_category/<int:cat_id>')
def delete_category(cat_id):
    if not is_admin():
        flash('Akses admin', 'danger')
        return redirect(url_for('login'))
    conn = connect_question(); cur = conn.cursor()
    cur.execute('DELETE FROM categories WHERE id=%s', (cat_id,))
    conn.commit(); cur.close(); conn.close()
    flash('Kategori dihapus (beserta pertanyaan terkait)', 'success')
    return redirect(url_for('admin.index'))
