from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, select, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///tasks.db')

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    duedate = Column(Date)
    complete = Column(Boolean, default=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def formatDate(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

def append(title, content, duedate):
    task = Task(title=title, content=content, duedate=formatDate(duedate))
    session.add(task)
    session.commit()

def readAll():
    tasks = session.query(Task).all()
    tasks_as_dict = [task.__dict__ for task in tasks]
    return tasks_as_dict

def getTaskById(id):
    stmt = select(Task).where(Task.id == id)
    task = session.scalar(stmt)
    return task

def str_to_bool(str_value):
    try:
        bool_value = bool(int(str_value))
    except (ValueError, TypeError):
        bool_value = False  # set a default value if the conversion fails
    return bool_value

def editComplete(id, new_bool):
    stmt = update(Task).where(Task.id == id).values(complete=str_to_bool(new_bool))
    session.execute(stmt)
    session.commit()

def editTitle(id, new_title):
    stmt = update(Task).where(Task.id == id).values(title=new_title)
    session.execute(stmt)
    session.commit()

def editContent(id, new_content):
    stmt = update(Task).where(Task.id == id).values(content=new_content)
    session.execute(stmt)
    session.commit()

def editDuedate(id, new_duedate):
    stmt = update(Task).where(Task.id == id).values(duedate=formatDate(new_duedate))
    session.execute(stmt)
    session.commit()

def editTask(id, field, value):
    if field == 'title':
        editTitle(id, value)
    elif field == 'content':
        editContent(id, value)
    elif field == 'duedate':
        editDuedate(id, value)
    elif field == 'complete':
        editComplete(id, value)
    else:
        print("UNEXPECTED FIELD IN DB UPDATE")

def deleteTask(id):
    stmt = delete(Task).where(Task.id == id)
    session.execute(stmt)
    session.commit()

