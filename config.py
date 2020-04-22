import os
SECRET_KEY = os.urandom(32)

# Folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#----------------------------------------------------------------------------#
# Database
#----------------------------------------------------------------------------#


SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/wmd'
#SQLALCHEMY_DATABASE_URI = 'postgres://abaqafjqjpygxw:6278eb22c84c9488c044a2727ec4a530bd8bb6cee5cf100913c6380c21ce256b@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d2efim24lu0f1q'

SQLALCHEMY_TRACK_MODIFICATIONS = False
