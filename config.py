import os
SECRET_KEY = os.urandom(32)

# Folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#----------------------------------------------------------------------------#
# Database
#----------------------------------------------------------------------------#

# SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/fyyur'

#Moved database to Cloud
SQLALCHEMY_DATABASE_URI = 'postgres://postgres@35.198.158.106:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
