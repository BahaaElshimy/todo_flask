from flask import Flask, jsonify, request
from db import db
from service.todo_service import Todo_Service
from model.todo import Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

todo_Service = Todo_Service()


@app.route("/")
def home():
    return "Hello Bahaa From todo"


# add todo

@app.route("/todo", methods=['POST'])
def save_todo():
    request_data = request.get_json()
    return jsonify(todo_Service.save(Todo(None, request_data['title'], request_data['done'])).serialize())


# retreivel all todos
@app.route("/todo", methods=['GET'])
def list_all_todo():
    print(todo_Service.list_todos())
    return jsonify([todo.serialize() for todo in todo_Service.list_todos()])


#  update todo to done
@app.route("/todo/<id>", methods=['PUT'])
def update_todo(id: int):
    request_data = request.get_json()
    return jsonify(todo_Service.update_todo(Todo(id, request_data['title'], request_data['done'])).serialize())


# delete Todo
@app.route("/todo/<id>", methods=['DELETE'])
def delete_todo(id: int):
    todo_Service.delete_todo(id)
    return jsonify({"message": "todo deleted successfully"})


# register user

# add user todo


if __name__ == '__main__':
    db.init_app(app)
    app.run()
