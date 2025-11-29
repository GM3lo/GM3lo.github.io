import os
import sqlite3
import uuid
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify, flash

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'ppt', 'pptx', 'txt', 'mp4', 'mp3', 'jpg', 'jpeg', 'png', 'gif', 'html'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id TEXT PRIMARY KEY,
            filename TEXT NOT NULL,
            original_name TEXT NOT NULL,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    conn = get_db()
    simulados = conn.execute('SELECT * FROM files WHERE category = "simulado" ORDER BY created_at DESC').fetchall()
    aulas = conn.execute('SELECT * FROM files WHERE category = "aula" ORDER BY created_at DESC').fetchall()
    materiais = conn.execute('SELECT * FROM files WHERE category = "material" ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', simulados=simulados, aulas=aulas, materiais=materiais)

@app.route('/simulado_vigilancia.html')
def simulado_vigilancia():
    return send_from_directory('.', 'simulado_vigilancia.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form.get('password')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        if password == admin_password:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Senha incorreta!')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

@app.route('/admin')
@admin_required
def admin_dashboard():
    conn = get_db()
    files = conn.execute('SELECT * FROM files ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('admin.html', files=files)

@app.route('/admin/upload', methods=['POST'])
@admin_required
def admin_upload():
    if 'file' not in request.files:
        flash('Nenhum arquivo selecionado')
        return redirect(url_for('admin_dashboard'))
    
    file = request.files['file']
    if file.filename == '':
        flash('Nenhum arquivo selecionado')
        return redirect(url_for('admin_dashboard'))
    
    if file and allowed_file(file.filename):
        file_id = str(uuid.uuid4())
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{file_id}.{ext}"
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        
        category = request.form.get('category', 'material')
        title = request.form.get('title', file.filename)
        description = request.form.get('description', '')
        
        conn = get_db()
        conn.execute('''
            INSERT INTO files (id, filename, original_name, category, title, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (file_id, filename, file.filename, category, title, description))
        conn.commit()
        conn.close()
        
        flash(f'Arquivo "{title}" enviado com sucesso!')
    else:
        flash('Tipo de arquivo não permitido')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/delete/<file_id>', methods=['POST'])
@admin_required
def admin_delete(file_id):
    conn = get_db()
    file = conn.execute('SELECT * FROM files WHERE id = ?', (file_id,)).fetchone()
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file['filename'])
        if os.path.exists(filepath):
            os.remove(filepath)
        conn.execute('DELETE FROM files WHERE id = ?', (file_id,))
        conn.commit()
        flash('Arquivo excluído com sucesso!')
    conn.close()
    return redirect(url_for('admin_dashboard'))

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
