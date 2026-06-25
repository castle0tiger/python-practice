from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("guestbook.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = sqlite3.connect("guestbook.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages")
    rows = cur.fetchall()
    conn.close()
    return render_template("guestbook.html", rows=rows)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    message = request.form["message"]
    conn = sqlite3.connect("guestbook.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)


