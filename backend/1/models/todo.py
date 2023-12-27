from sqlalchemy import Column, Integer, String
from db.config import Base


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Todo {self.title}>"

    def to_dict(self):
        return dict(id=self.id, title=self.title, content=self.content)
