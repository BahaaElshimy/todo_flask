from repository.todo_repository import Todo_Repository
from model.todo import Todo

class Todo_Service:
    def __init__(self):
        self.todo_repo = Todo_Repository()

    def save(self, todo:Todo) -> Todo:
        return self.todo_repo.save_todo(todo)

    def list_todos(self):
        return self.todo_repo.list_todos()

    def update_todo(self,todo:Todo) -> Todo:
        return self.todo_repo.update_todo( todo)

    def delete_todo(self, id):
        return self.todo_repo.delete_todo(id)
