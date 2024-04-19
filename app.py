from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r"C:\Users\dhyey\Documents\Python111\Project 6")
db_name = "Prime_TV_Shows_Data_set.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.link.html") 

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/data.html")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    students = cursor.execute("SELECT * FROM Prime_Shows").fetchall()
    con.close()

    return render_template("data_table.html", students=students)

if __name__=="__main__":
    app.run(debug=True)