# configuration file for flaskTaskerII 

import os

# get the folder where this script lives
basedir =  os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flaskTaskerII.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

# define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
