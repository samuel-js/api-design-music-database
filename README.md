
# Casting Agency API

This project is my first step to a fully developed web application following `Udacity Fullstack Developer Nanodegree` guidelines. It's a web app for a casting agency where users can add movies, actors, and relate each actor to the movies he acted in, and vice versa. This project uses python, flask and postgresql for it's backend and hosted on heruko. 

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

No frontend is developed for this app, you can use it using cURL or [Postman](https://www.postman.com)


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


## Running the server

first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development

To run the app 
  alt. 1: flask run (runs de server on port 5000)
  alt. 2: python app.py (runs de server on port 8100)


```
Sourcing `setup.sh` sets some environment variables used by the app.

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the this file to find the application.


## API Reference

### Getting Started

- Base URL: You can run this API locally at the default `http://127.0.0.1:5000/`
- Authentication: This app has 3 users. Each has his own token which are provided in `setup.sh` file. Details about each user privlages are provided below.

### Endpoints

## Link to Postman Documentation
Endpoint routes and examples can be found here:
[Postman Documentation](https://documenter.getpostman.com/view/10357939/Szf6YUHZ)


- GET '/Records'
- GET '/Artists'
- POST '/Records'
- POST '/Artists'
- PATCH '/Records/<int:id>'
- PATCH '/Artists/<int:id>'
- DELETE '/Records/<int:id>'
- DELETE '/Artists/<int:id>'

### Users

This app has 3 users. each user has his own privileges.

- Manager
	- Permissions to all endpoints

- Editor
	- access:site	access:site	
  - get:artist-details	
  - get:artists		
  - get:record-details		
  - get:records		
  - patch:artists		
  - patch:records		
  - post:artists		
  - post:records	

- Visitor
	- No permissions

Please Note, to use any endpoint, you must send the request with user access token in Authorization header, which are provided in `setup.sh`.


## Testing

To run the tests, run
```
dropdb capstone_test
createdb capstone_test
python test_app.py
```

## Deployment

This app is deployed on heruko under this [link](https://capstone-fsnd-which-not-taken.herokuapp.com/).
