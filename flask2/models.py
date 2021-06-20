from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import LargeBinary
from database import Base

class User(Base):
    # table name
    __tablename__ = 'users'

    # attribute
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    state = Column(String(32))
    salary = Column(Integer)
    grade = Column(Integer)
    room = Column(String(32))
    telnum = Column(String(32))
    picture = Column(LargeBinary)
    keywords = Column(String(300))

    def __init__(self, name=None, state=None,
    salary=None, grade=None, room=None, telnum=None, picture=None, keywords=None):
        self.name = name
        self.state = state
        self.salary = salary
        self.grade = grade
        self.room = room
        self.telnum = telnum
        self.picture = picture
        self.keywords = keywords



    def __repr__(self):
        return '<User %r>' % (self.name)
