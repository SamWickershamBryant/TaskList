from flask import Flask, render_template, request, redirect, url_for
from forms import AddTaskForm
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Put Secret String Here!'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET","POST"])
def hello_world():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
      
       
    form = AddTaskForm()
    return render_template("main.html", tasks=tasks, form=form)

@app.route("/add", methods=["GET","POST"])
def add():
    conn = get_db_connection()
    print(request.form)
    if request.method == "POST":
        taskname = request.form.get("taskname")
        taskcontent = request.form.get("taskcontent")
        duedate = request.form.get("duedate")
        if taskname and taskcontent and duedate:
            conn.execute('INSERT INTO tasks (title, content, duedate) VALUES (?, ?, ?)',
            (taskname, taskcontent, duedate))
            conn.commit()
            conn.close()
    return redirect("/")

@app.route("/delete", methods=["GET","POST"])
def delete():
    if request.method == "POST":
        conn = get_db_connection()
        print(request.form)
        deleteid = request.form['id']

        conn.execute('DELETE FROM tasks WHERE id=' + deleteid)
        conn.commit()
        conn.close()
    return redirect("/")

@app.route("/edit", methods=["GET","POST"])
def edit():
    conn = get_db_connection()
    
    if request.method == "POST":
        print(request.form)
        
        field = request.form['field']
        value = request.form['value']
        editid = request.form['id']



        conn.execute('UPDATE tasks SET ' + field + ' = ? WHERE id = ?',
        (value, editid))
        
        conn.commit()
        conn.close()
    return redirect("/")
        

    


