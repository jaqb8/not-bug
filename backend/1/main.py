from flask import Flask, jsonify, request
import pydantic
import werkzeug
from db.config import init_db, db_session
from dto.todo_dto import TodoDto
from services.todo_service import get_todo_service


app = Flask("todo-api")
init_db()
service = get_todo_service()


@app.route("/")
def index():
    return "Todo API"


@app.route("/todos", methods=["GET"])
def get_todos():
    todos = service.get_all_todos()
    return jsonify([todo.to_dict() for todo in todos]), 200


@app.route("/todos", methods=["POST"])
def create_todo():
    todo_dto = TodoDto(**request.json)
    todo = service.create_todo(title=todo_dto.title, content=todo_dto.content)
    return jsonify(todo.to_dict()), 201


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int):
    todo = service.get_todo_by_id(todo_id)
    return jsonify(todo.to_dict()), 200


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id: int):
    todo_dto = TodoDto(**request.json)
    todo = service.update_todo(
        todo_id=todo_id,
        title=todo_dto.title,
        content=todo_dto.content,
    )
    return jsonify(todo.to_dict()), 200


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    service.delete_todo(todo_id)
    return jsonify({"message": "Todo deleted"}), 200


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(_: werkzeug.exceptions.NotFound):
    return jsonify({"message": "Todo not found"}), 404


@app.errorhandler(werkzeug.exceptions.MethodNotAllowed)
def handle_method_not_allowed(_: werkzeug.exceptions.MethodNotAllowed):
    return jsonify({"message": "Method not allowed"}), 405


@app.errorhandler(pydantic.ValidationError)
def handle_validation_error(e: pydantic.ValidationError):
    errors = [{"message": err["msg"], "loc": err["loc"]} for err in e.errors()]
    return jsonify({"errors": errors}), 400


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(debug=True)
