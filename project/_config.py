# configuration file for flaskTaskerII 

import os

# get the folder where this script lives
basedir =  os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flaskTaskerII.db'
#USERNAME = 'admin'
#PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

SQLALCHEMY_TRACK_MODIFICATIONS = True 
DEBUG = False