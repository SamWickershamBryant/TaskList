from flask import Flask, render_template, request, redirect, url_for
from forms import AddTaskForm
from database import append, readAll, editTask, deleteTask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Put Secret String Here!'


@app.route("/", methods=["GET","POST"])
def hello_world():
    
    tasks = readAll()
      
       
    form = AddTaskForm()
    return render_template("main.html", tasks=tasks, form=form)

@app.route("/add", methods=["GET","POST"])
def add():
    print(request.form)
    form = AddTaskForm(request.form)
    #import pdb
    #pdb.set_trace()
    if form.validate_on_submit():
        print("WORKS")
        taskname = request.form.get("taskname")
        taskcontent = request.form.get("taskcontent")
        duedate = request.form.get("duedate")
        if taskname and taskcontent and duedate:
            append(taskname, taskcontent, duedate)
    return redirect("/")

@app.route("/delete", methods=["GET","POST"])
def delete():
    if request.method == "POST":
        print(request.form)
        deleteid = request.form['id']
        deleteTask(deleteid)
    return redirect("/")

@app.route("/edit", methods=["GET","POST"])
def edit():
    
    if request.method == "POST":
        print(request.form)
        
        field = request.form['field']
        value = request.form['value']
        editid = request.form['id']
        
        editTask(editid, field, value)

    return redirect("/")
        

    


