
# Casting Agency API

This project is an API tha works as a backend for a music databse. The database is very simple and have only two tables: Records and Artists. Throug the API you can consult the database, create, edit and delete records. There is an almost ready front end developed but I won't publish it until it's fully working. The only part that is left to implement is the authorization in the front end, which is taking to long to put in place. I'll update this repo whe it's finished.

## Deployment
This app is deployed on heruko under this [link](/).

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
- `setup.sh` sets some environment variables used by the app.
- Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
- Setting the `FLASK_APP` variable to `app.py` directs flask to use this file to find the application.

## API Reference

### Getting Started

- Base URL: You can run this API locally at the default `http://127.0.0.1:5000/`
- Authentication: This app has 3 users. Each has his own token which are provided in `setup.sh` file. Details about each user privlages are provided below.

### Users
This app has 3 users. each user has his own privileges.
- Manager
	- Permissions to all endpoints includind deleting records
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
	- Permision only to vitit the base url

### Endpoints
## Link to Postman Documentation
Endpoint routes and examples can be found here:
[Postman Documentation](https://documenter.getpostman.com/view/10357939/Szf6YUHZ)
To test the endpoints, you must send the request with user access token in Authorization header, which are provided in `setup.sh`.

- GET '/Records'
- GET '/Artists'
- POST '/Records'
- POST '/Artists'
- PATCH '/Records/<int:id>'
- PATCH '/Artists/<int:id>'
- DELETE '/Records/<int:id>'
- DELETE '/Artists/<int:id>'

## Testing
To run the tests, run
```
dropdb wmd_test
createdb wmd_test
psql wmd_test < wmd_test.sql
python test_app.py
```

## Deployment
This app is deployed on heruko under this [link](/).
