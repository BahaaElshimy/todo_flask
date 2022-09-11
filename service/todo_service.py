from repository.todo_repository import Todo_Repository
from model.todo import Todo

class Todo_Service:
    def __init__(self):
        self.todo_repo = Todo_Repository()

    def save(self, todo:Todo) -> Todo:
        try:
            return self.todo_repo.save_todo(todo)
        except:
            return {"message":"can't save todo {}".format(todo)}

    def list_todos(self):
        try:
            return self.todo_repo.list_todos()
        except:
          return {"message":"Exception occured "}

    def update_todo(self,todo:Todo) -> Todo:
        item  = Todo.query.filter_by(id=todo.id).first()
        if item:
            item.title = todo.title
            item.done = todo.done
            return self.todo_repo.save_todo(item)

        return {"message":"Item doesn't exist"}

    def delete_todo(self, id):
        return self.todo_repo.delete_todo(id)
