from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Todo {}>".format(self.task)
