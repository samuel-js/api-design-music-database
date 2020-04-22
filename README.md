
# Introduction

This project is an API tha works as a backend for a music databse. The database is very simple and have only two tables: Records and Artists. Throug the API you can consult the database, create, edit and delete records. There is an almost ready front end developed but I won't publish it until it's fully working. The only part that is left to implement is the authorization in the front end, which is taking to long to put in place. I'll update this repo whe it's finished.

## Deployment
This app is deployed and hosted at Heroku [here](https://world-music-database.herokuapp.com/).
 
## Getting Started

### Installing Dependencies

#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
#### Virtual Enviornment
I recommend working within a virtual environment whenever using Python for projects. This keeps dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for the platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

### Understanding the project's structure
```
├── Procfile
├── README.md
├── app.py
├── app_tests.py
├── auth.py
├── config.py
├── error.log
├── fabfile.py
├── manage.py
├── migrations
├── models.py
├── requirements.txt
├── setup.sh
└── wmd_test.sql"
```

## Running the server
To run the server, execute:
```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run 
```

## API Reference
- Authentication: This app has 3 users, two with permissions and one without permissions. Tokens are provided in `setup.sh` file. Details about each user privlages are provided below.

### Users
This app has 3 users, each user has his own privileges.
- Manager
  - Permissions to all endpoints including deleting entries from the database
  -delete:artists		
  -delete:records
- Editor
  - get:artist-details	
  - get:artists		
  - get:record-details		
  - get:records		
  - patch:artists		
  - patch:records		
  - post:artists		
  - post:records	
- Visitor
	- Permision only to vitit the base url https://world-music-database.herokuapp.com

### Endpoints

- GET '/Records'
- GET '/Artists'
- POST '/Records'
- POST '/Artists'
- PATCH '/Records/<int:id>'
- PATCH '/Artists/<int:id>'
- DELETE '/Records/<int:id>'
- DELETE '/Artists/<int:id>'

## Link to Postman Documentation
Endpoint routes and examples can be found here:
[Postman Documentation](https://documenter.getpostman.com/view/10357939/Szf9VSUr)

To test the endpoints, you must send the request with user access token in Authorization header, which are provided in `setup.sh`. If the token expires, new tokens can be obtained for the "Editor" roll at the [Authorization page](https://sanabria.eu.auth0.com/authorize?audience=wmd-api&response_type=token&client_id=gcSZ07udVbxJHpvQBvkzqOdpkI9ik6Ol&redirect_uri=https://world-music-database.herokuapp.com)

## Testing
To run the tests, run
```
dropdb wmd_test
createdb wmd_test
psql wmd_test < wmd_test.sql
python test_app.py
```

