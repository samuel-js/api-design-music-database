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
#SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/wmd'
SQLALCHEMY_DATABASE_URI = 'postgres://funjsyvgfhftud:8ffa1545e5dc86e7ac59fb0bd569466fae5dedc998e0f396f2cf0f2a4607e4f6@ec2-3-223-21-106.compute-1.amazonaws.com:5432/dfbu7shn383euk'

SQLALCHEMY_TRACK_MODIFICATIONS = False
