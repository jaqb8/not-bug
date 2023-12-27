import os
import pytest
import werkzeug
from main import app
from models.todo import Todo


@pytest.fixture
def client(mocker):
    with app.test_client() as client:
        mocker.patch("models.todo.Todo.query", return_value=True)
        yield client


def test_index(client):
    res = client.get("/")
    assert "Todo API" in res.text
    assert res.status_code == 200


def test_get_todos(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.get_all_todos",
        return_value=[Todo(), Todo()],
    )

    res = client.get("/todos")
    assert res.status_code == 200
    assert len(res.json) == 2


def test_create_todo_success(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.create_todo",
        return_value=Todo(
            title="test",
            content="test",
        ),
    )

    res = client.post("/todos", json={"title": "test", "content": "test"})
    assert res.status_code == 201
    assert res.json["title"] == "test"
    assert res.json["content"] == "test"


def test_create_todo_missing_title(client):
    res = client.post("/todos", json={"content": "test"})
    assert res.status_code == 400


def test_create_todo_missing_content(client):
    res = client.post("/todos", json={"title": "test"})
    assert res.status_code == 400


def test_get_todo_success(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.get_todo_by_id",
        return_value=Todo(
            title="test",
            content="test",
        ),
    )

    res = client.get("/todos/1")
    assert res.status_code == 200
    assert res.json["title"] == "test"
    assert res.json["content"] == "test"


def test_get_todo_not_found(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.get_todo_by_id",
        side_effect=werkzeug.exceptions.NotFound(),
    )

    res = client.get("/todos/1")
    assert res.status_code == 404


def test_update_todo_success(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.update_todo",
        return_value=Todo(
            title="test",
            content="test",
        ),
    )

    res = client.put("/todos/1", json={"title": "test", "content": "test"})
    assert res.status_code == 200
    assert res.json["title"] == "test"
    assert res.json["content"] == "test"


def test_update_todo_not_found(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.update_todo",
        side_effect=werkzeug.exceptions.NotFound(),
    )

    res = client.put("/todos/1", json={"title": "test", "content": "test"})
    assert res.status_code == 404


def test_delete_todo_success(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.delete_todo",
    )

    res = client.delete("/todos/1")
    assert res.status_code == 200
    assert res.json["message"] == "Todo deleted"


def test_delete_todo_not_found(client, mocker):
    mocker.patch(
        "services.todo_service.TodoService.delete_todo",
        side_effect=werkzeug.exceptions.NotFound(),
    )

    res = client.delete("/todos/1")
    assert res.status_code == 404
