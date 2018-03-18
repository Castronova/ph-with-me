from sqlalchemy import Column, Integer, String, Date
from datetime import datetime as dt
from app.server.database import Base


class ChatSession(Base):
    __tablename__ = 'chat_session'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    admin = Column(String(120), unique=False)
    created = Column(Date, unique=False)

    def __init__(self, name=None, admin=None):
        self.name = name
        self.admin = admin
        self.created = dt.now()

    def __repr__(self):
        return '<Chatroom %r>' % (self.name)
