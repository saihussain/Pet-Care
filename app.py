<<<<<<< HEAD

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
=======
from flask import Flask
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        conn.close()
        return "✅ Pet-Care Database Connected Successfully!"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":