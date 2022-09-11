from db import db


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    done = db.Column(db.Integer)

    def __init__(self, id, title, done):
        self.title = title
        self.done = done
        self.id = id

    def __str__(self):
        return f"Todo(title={self.title},done{self.done})"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }
