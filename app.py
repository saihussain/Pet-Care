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
    app.run(debug=True)