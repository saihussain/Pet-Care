from database import get_db_connection

try:
    conn = get_db_connection()
    print("✅ Database Connected Successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")

    db = cursor.fetchone()
    print("Connected to:", db[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)