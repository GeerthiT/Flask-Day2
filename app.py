from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("To-Do.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    new_task = Todo(task=task)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:task_id>")
def update(task_id):
    task = Todo.query.get(task_id)
    if task:
        task.done = not task.done
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Todo.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
