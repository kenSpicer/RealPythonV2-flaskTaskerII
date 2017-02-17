# flaskTaskerII/project/db_create.py 

from views import db 
from models import Task, User
from datetime import date


# create the database and the db table
db.create_all()

# insert the data
db.session.add(Task('Finish this tutorial', date(2017, 3, 24), 10, date.today(), 1, 1))
db.session.add(Task('Finish Real Python', date(2017, 9, 24), 10, date.today(), 1, 1))

# commit the changes
db.session.commit()



