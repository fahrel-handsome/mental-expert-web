from db.database_auth import connect_auth
import hashlib

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def register_user(nama, email, password, role='user'):
    conn = connect_auth()
    cur = conn.cursor()
    pw_h = hash_password(password)
    try:
        cur.execute("INSERT INTO users (nama, email, password, role) VALUES (%s,%s,%s,%s)",
                    (nama, email, pw_h, role))
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        cur.close()
        conn.close()

def verify_user(email, password):
    conn = connect_auth()
    cur = conn.cursor()
    pw_h = hash_password(password)
    cur.execute("SELECT id, nama, role FROM users WHERE email=%s AND password=%s", (email, pw_h))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row  # None or (id,nama,role)
