from flask import Flask, render_template
import sqlite3
import pandas as pd
import threading

app = Flask(__name__)

# Function to get data from the database
def get_data(sample_size=10):
    conn = sqlite3.connect(r"C:\Users\canze\Documents\DAB111\.venv\Python\Python P1\Database\student_data.db")  # Adjust the path to where your DB is
    query = f"SELECT * FROM students LIMIT {sample_size}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    df = get_data(10)
    return render_template("data.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route("/details")
def details():  # Change function name to 'details' to match the correct route
    return render_template("details.html")

# Running the Flask app in a separate thread
def run_app():
    app.run(debug=True, use_reloader=False)  # `use_reloader=False` prevents the notebook from restarting itself

if __name__ == "__main__":
    # Start the app in a separate thread to avoid blocking
    thread = threading.Thread(target=run_app)
    thread.start()