# Code references:
# User CrazyGuitar: SQLAlchemy https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-sqlalchemy.rst#set-a-database-url
# Constraints: https://docs.sqlalchemy.org/en/13/core/constraints.html
# Multiple Constraints: https://gist.github.com/asyd/3cff61ed09eabe187d3fbec2c8a3ee39
# Flash Messages not displayed: https://stackoverflow.com/questions/49012562/flask-one-flash-message-not-getting-displayed
# Remove Password: https://dba.stackexchange.com/questions/83164/remove-password-requirement-for-user-postgres
# Split Flask Models: https://stackoverflow.com/questions/34281873/how-do-i-split-flask-models-out-of-app-py-without-passing-db-object-all-over

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
from datetime import datetime
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import sys

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# class Venue
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    #genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'), nullable=True)
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))

    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
        return f'<Venue {self.id} {self.name} {self.image_link}>'

# class Artist
#----------------------------------------------------------------------------#

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    #genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'), nullable=True)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))

    shows = db.relationship('Show', backref='artist', lazy=True)
    genres = db.relationship('Genre', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.id} {self.name} {self.image_link}>'

# class Show
#----------------------------------------------------------------------------#

class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Show {self.id}, Artist {self.artist_id}, Artist {self.image_link}, Venue {self.venue_id}>'

# class Genre (Didn't use it at the end)
#----------------------------------------------------------------------------#
class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')

#  Venues
#----------------------------------------------------------------------------#
# Code ref. Nicholas Pretorius

@app.route('/venues')
def venues():
  venue_list = Venue.query.all()

  venues_dict = {}

  for venue in venue_list:
    key = f'{venue.city}, {venue.state}'

    venues_dict.setdefault(key, []).append({
        'id': venue.id,
        'name': venue.name,
        'num_upcoming_shows': len(venue.shows),
        'city': venue.city,
        'state': venue.state
      })

  data = []
  for value in venues_dict.values():
      data.append({
        'city': value[0]['city'],
        'state': value[0]['state'],
        'venues': value
      }) 

  return render_template('pages/venues.html', areas=data);

#  Venue Search
#----------------------------------------------------------------------------#
# Code ref. Ovie Mudi

@app.route('/venues/search', methods=['POST'])
def search_venues():

  search_term = request.form.get('search_term', '')
  venue_search_result = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).all()
  
  response={
    "count": len(venue_search_result),
    "data": []   
    }

  for result in venue_search_result:
      response["data"].append({
        "id": result.id,
        "name": result.name,
        "num_upcoming_shows": len(result.shows)
      })

  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

#  Venue Show
#----------------------------------------------------------------------------#

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  
  # Query Artist table (SELECT * FROM Artist FILTER BY id)
  venue = Venue.query.filter_by(id=venue_id).first()

  past_shows = []
  upcoming_shows = []
  
  # Create empty lists for past and upcoming shows
  show_attributes = None
  for show in venue.shows:
    show_attributes = {
      "artist_id": show.artist.id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": show.start_time.strftime('%m/%d/%Y, %H:%M:%S')
    }

    if show.start_time <= datetime.now():
      past_shows.append(show_attributes)
    else:
      upcoming_shows.append(show_attributes)

  venue_dict = {
    "id": venue.id,
    "name": venue.name,
    "genres": venue.genres,
    "address": venue.address,
    "city": venue.city,
    "state": venue.state,
    "phone": venue.phone,
    "website": venue.website,
    "facebook_link": venue.facebook_link,
    "image_link": venue.image_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description": venue.seeking_description, 
    "past_shows": past_shows,
    "upcoming_shows": upcoming_shows,
    "past_shows_count": len(past_shows),
    "upcoming_shows_count": len(upcoming_shows)
  }

  return render_template('pages/show_venue.html', venue=venue_dict)

#  Venue Create
#----------------------------------------------------------------------------#

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  new_venue = Venue(
    name=request.form['name'],
    city=request.form['city'],
    state=request.form['state'],
    address=request.form['address'],
    phone=request.form['phone'],
    genres=request.form.getlist('genres'),
    facebook_link=request.form['facebook_link'],
    image_link=request.form['image_link']
  )

  try:
    db.session.add(new_venue)
    db.session.commit()
    flash('The venue ' + request.form['name'] + ' was successfully listed!')

  except:
    flash('An error occurred. Venue ' + new_venue.name + ' could not be listed.', category='error')
    print('exc_info()', exc_info())
    db.session.rollback()
  
  finally:
    db.session.close()
    return redirect(url_for('venues'))  

#  Venue Delete
#----------------------------------------------------------------------------#

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  #status = False
  try:
    venue = Venue.query.get(venue_id)
    db.session.delete(venue)
    db.session.commit()
    #status = True
    flash('The venue ' + request.form['name'] + ' was successfully deleted!')

  except:
    flash('An error occurred. Venue ' + new_venue.name + ' could not be deleted.', category='error')
    print('exc_info()', exc_info())
    db.session.rollback()
  
  finally:
    db.session.close()
    return redirect(url_for('/')) 

#  Artists
#----------------------------------------------------------------------------#
@app.route('/artists')

def artists():
  data = []
  artists = Artist.query.all()

  for artist in artists:
      data.append({
          "id": artist.id,
          "name": artist.name
      })

  return render_template('pages/artists.html', artists=data)

#  Artists Search
#----------------------------------------------------------------------------#

@app.route('/artists/search', methods=['POST'])
def search_artists():
  search_term = request.form.get('search_term', '')
  artist_search_result = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()
  response={
    "count": len(artist_search_result),
    "data": []   
    }

  for result in artist_search_result:
      response["data"].append({
        "id": result.id,
        "name": result.name,
        "num_upcoming_shows": len(result.shows)
      })

  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

# Artist Page Show
#----------------------------------------------------------------------------#

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
      
# Query Artist table (SELECT * FROM Artist ORDER BY id)
  artist = Artist.query.filter_by(id=artist_id).first()

# Create empty lists for past and upcoming shows
  past_shows = []
  upcoming_shows = []

# Create a dictionary with Show details
  show_details = None
  for show in artist.shows:
    show_details = {
      "venue_id": show.venue.id,
      "venue_name": show.venue.name,
      "venue_image_link": show.venue.image_link,
      "start_time": show.start_time.strftime('%m/%d/%Y, %H:%M:%S')
    }
   
# Populate lists with Show details depending on date 
    if show.start_time <= datetime.now():
      past_shows.append(show_details)
    else:
      upcoming_shows.append(show_details)

# Artist data to be displayed
  artist_dict = {
      "id": artist.id,
      "name": artist.name,
      "genres": artist.genres,
      "city": artist.city,
      "state": artist.state,
      "phone": artist.phone,
      "website": artist.website,
      "facebook_link": artist.facebook_link,
      "image_link": artist.image_link,
      "seeking_venue": artist.seeking_venue,
      "seeking_description": artist.seeking_description, 
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": len(past_shows),
      "upcoming_shows_count": len(upcoming_shows)
    }

  return render_template('pages/show_artist.html', artist=artist_dict)

# Artist Edit
#----------------------------------------------------------------------------#
# Code ref. Tune Dev

@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm(request.form)
  artist = Artist.query.filter_by(id=artist_id).first()

  form.name.process_data(artist.name)
  form.city.process_data(artist.city)
  form.phone.process_data(artist.phone)
  form.state.process_data(artist.state)
  form.genres.process_data(artist.genres)
  form.facebook_link.process_data(artist.facebook_link)
  form.image_link.process_data(artist.image_link)

  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  artist = Artist.query.filter_by(id=artist_id).first()
  try:
      artist.name = request.form['name']
      artist.city = request.form['city']
      artist.state = request.form['state']
      artist.phone = request.form['phone']
      artist.genres = request.form.getlist('genres')
      artist.facebook_link = request.form['facebook_link']
      artist.image_link = request.form['image_link']

      db.session.commit()
      flash('The artist ' + request.form['name'] + ' was successfully updated!')
  except:
      flash('An error occurred. Artist ' +
            request.form['name'] + ' could not be updated')
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()
  return redirect(url_for('show_artist', artist_id=artist_id))  

# Venue Edit
#----------------------------------------------------------------------------#

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm(request.form)
  venue = Venue.query.filter_by(id=venue_id).first()
  
  form.name.process_data(venue.name)
  form.city.process_data(venue.city)
  form.phone.process_data(venue.phone)
  form.state.process_data(venue.state)
  form.genres.process_data(venue.genres)
  form.facebook_link.process_data(venue.facebook_link)
  form.image_link.process_data(venue.image_link)

  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  venue = Venue.query.filter_by(id=venue_id).first()
  try:
    venue.name = request.form['name']
    venue.city = request.form['city']
    venue.state = request.form['state']
    venue.phone = request.form['phone']
    venue.genres = request.form.getlist('genres')
    venue.facebook_link = request.form['facebook_link']
    venue.image_link = request.form['image_link']

    db.session.commit()
    flash('The venue ' + request.form['name'] + ' was successfully updated!')
  except:
      flash('An error occurred. Venue ' +
            request.form['name'] + ' could not be updated')
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Artist Create
#----------------------------------------------------------------------------#

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  new_artist = Artist(
    name=request.form['name'],
    city=request.form['city'],
    state=request.form['state'],
    phone=request.form['phone'],
    genres=request.form.getlist('genres'),
    facebook_link=request.form['facebook_link'],
    image_link=request.form['image_link']
  )

  try:
    db.session.add(new_artist)
    db.session.commit()
    flash('The artist ' + request.form['name'] + ' was successfully listed!')

  except:
    flash('An error occurred. The artist ' + new_artist.name + ' could not be listed.', category='error')
    print('exc_info(): ', exc_info())
    db.session.rollback()

  finally:
    db.session.close()
    return redirect(url_for('artists'))
  

# Shows
#----------------------------------------------------------------------------#
# Code ref. Ivan Canales

@app.route('/shows')
def shows():
  data = []
  show_list = Show.query.all()

  for show in show_list:
    data.append({
      "venue_id": show.venue_id,
      "venue_name": Venue.query.filter_by(id=show.venue_id).first().name,
      "artist_id": show.artist_id, 
      "artist_name": Artist.query.filter_by(id=show.artist_id).first().name,
      "artist_image_link": show.artist.image_link, 
      'start_time': show.start_time.strftime('%Y-%m-%d, %H:%M:%S')
    })

  return render_template('pages/shows.html', shows=data)

#  Shows Create
#----------------------------------------------------------------------------#

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  new_show = Show(
    artist_id=request.form['artist_id'],
    venue_id=request.form['venue_id'],
    start_time=request.form['start_time']
  )
  
  try:
    db.session.add(new_show)
    db.session.commit()
    flash('The Show at' + request.form['venue_name'] + ' was successfully listed!')

  except:
    flash('An error occurred. Artist ' + new_artist.name + ' could not be listed.', category='error')
    print('exc_info(): ', exc_info())
    db.session.rollback()

  finally:
    db.session.close()
    return redirect(url_for('shows'))

#----------------------------------------------------------------------------#
# Errors
#----------------------------------------------------------------------------#

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
