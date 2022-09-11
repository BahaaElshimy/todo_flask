from model.todo import  Todo
from typing import List
from db import  db

class Todo_Repository:

     def save_todo(self, todo:Todo) -> Todo:
         db.session.add(todo)
         db.session.commit()
         return todo

     def find_by_title(self, todo_title:str) -> Todo:
          return Todo.query.filter_by(title=todo_title).first()

     def list_todos(self) -> List[Todo]:
        return Todo.query.all()


     def delete_todo(self, id: int):
         Todo.query.filter_by(id=id).delete()
         db.session.commit()