from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='task name')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

today = datetime.today()


def add_task(new_task, new_deadline):
    new_row = Table(task=new_task,
                    deadline=datetime.strptime(new_deadline, '%Y-%m-%d').date())
    session.add(new_row)
    session.commit()
    print('The task has been added!')


def current_tasks(num_day):
    current_day = today + timedelta(days=num_day)
    rows = session.query(Table).filter(Table.deadline == current_day.date()).order_by(Table.deadline).all()
    if rows:
        for i in range(len(rows)):
            current_row = rows[i]
            print(f'{i + 1}. {current_row.task}')
    else:
        print('Nothing to do!')


def week_tasks():
    for i in range(7):
        current_day = today + timedelta(days=i)
        current_weekday = {0: 'Monday',
                           1: 'Tuesday',
                           2: 'Wednesday',
                           3: 'Thursday',
                           4: 'Friday',
                           5: 'Saturday',
                           6: 'Sunday'}[current_day.weekday()]
        print(f"\n{current_weekday} {current_day.day} {current_day.strftime('%b')}:")
        current_tasks(i)


def all_tasks(filter_tasks='all'):
    if filter_tasks == 'missed':
        rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    else:
        rows = session.query(Table).order_by(Table.deadline).all()
    if rows:
        for i in range(len(rows)):
            current_row = rows[i]
            print(f"{i + 1}. {current_row.task}. {current_row.deadline.day} {current_row.deadline.strftime('%b')}")
    else:
        print('Nothing to do!')
    return rows


def delete_task():
    print('Choose the number of the task you want to delete:')
    session.delete(all_tasks()[int(input('>'))-1])
    session.commit()
    print('The task has been deleted!')


def menu():
    while True:
        print(r'''
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit''')
        action = int(input('> '))
        if action == 1:
            print(f"\nToday {today.day} {today.strftime('%b')}:")
            current_tasks(0)
        elif action == 2:
            week_tasks()
        elif action == 3:
            print('\nAll tasks:')
            all_tasks()
        elif action == 4:
            print('\nMissed tasks:')
            all_tasks('missed')
        elif action == 5:
            add_task(input('Enter task\n>'), input('Enter deadline\n>'))
        elif action == 6:
            delete_task()
        else:
            print('Bye!')
            break


menu()
