import os
SECRET_KEY = os.urandom(32)

# Folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#----------------------------------------------------------------------------#
# Database
#----------------------------------------------------------------------------#

#Moved database to Cloud
SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/wmd'
SQLALCHEMY_TRACK_MODIFICATIONS = False
