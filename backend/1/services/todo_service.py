from typing import List
from models.todo import Todo
from db.config import db_session
from werkzeug.exceptions import NotFound


class TodoService:
    def create_todo(self, title: str, content: str) -> Todo:
        todo = Todo(title=title, content=content)
        db_session.add(todo)
        db_session.commit()
        return todo

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        todo = Todo.query.get(todo_id)
        if not todo:
            raise NotFound()
        return todo

    def get_all_todos(self) -> List[Todo]:
        return Todo.query.all()

    def update_todo(self, todo_id: int, title: str = None, content: str = None) -> Todo:
        todo = Todo.query.get(todo_id)
        if not todo:
            raise NotFound()

        todo.title = title if title else todo.title
        todo.content = content if content else todo.content
        db_session.commit()
        return todo

    def delete_todo(self, todo_id: int) -> None:
        todo = Todo.query.get(todo_id)
        if not todo:
            raise NotFound()

        db_session.delete(todo)
        db_session.commit()


def get_todo_service() -> TodoService:
    return TodoService()
