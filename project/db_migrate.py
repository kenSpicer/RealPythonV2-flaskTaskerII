# flaskTaskerII/project/db_migrate.py 

from views import db 
from _config import DATABASE_PATH
import sqlite3

with sqlite3.connect(DATABASE_PATH) as connection:
	# instantiate a cursor object
	c = connection.cursor()

	# temporarily change name of users table
	c.execute("""ALTER TABLE users RENAME TO old_users""")

	# create a new users table with updated schema
	db.create_all()

	# retrieve the data from the old_users table
	c.execute("""SELECT name, email, password FROM old_users
		ORDER BY id ASC""")

	# save all rows as a list of tuples; set role to 'user'
	data = [(row[0], row[1], row[2], 'user') for row in c.fetchall()]

	# insert data into users table
	c.executemany("""INSERT INTO users (name, email, password, role)
		VALUES (?,?,?,?)""", data)

	# delete old users table
	c.execute("DROP TABLE old_users")


