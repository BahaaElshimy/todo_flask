import sqlite3
import util
from model.todo import  Todo
from typing import List

class Todo_Repository:

     def map_row_to_todo(self, row):
          return Todo(row[0], row[1],row[2])

     def save_todo(self, todo:Todo) -> Todo:
         connection = util.getConnection()
         cursor = connection.cursor()
         cursor.execute('insert into todo (title , done) values(?,?)', (todo.title,todo.done))
         connection.commit()
         connection.close()
         todo.id = cursor.lastrowid
         return todo

     def find_by_title(self, todo_title:str) -> Todo:
         connection  = util.getConnection()
         cursor =  connection.cursor()
         row = cursor.execute('select title,done from todo where title =? ', (todo_title,)).fetchone()
         if row:
              return self.map_row_to_todo(row)

     def list_todos(self) -> List[Todo]:
         todos = []
         connection  = util.getConnection()
         cursor =  connection.cursor()
         for row in  cursor.execute('select id ,title,done from todo').fetchall():
              todos.append(self.map_row_to_todo(row))
         return todos

     def update_todo(self,  todo:Todo) ->Todo:
          connection = util.getConnection()
          cursor = connection.cursor()
          cursor.execute('update todo set title =? , done =? where id =?', (todo.title, todo.done, todo.id))
          connection.commit()
          connection.close()
          return todo

     def delete_todo(self, id: int):
          connection = util.getConnection()
          cursor = connection.cursor()
          cursor.execute('delete from todo where id =?', (id,))
          connection.commit()
          connection.close()
