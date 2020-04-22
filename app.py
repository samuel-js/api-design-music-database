#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
import sys
import json
from flask import Flask, request, Response, jsonify, abort, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from auth import requires_auth, AuthError
from models import setup_db, db, Record, Artist

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

def create_app(test_config=None):
    app = Flask(__name__)
    # Cors app
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

    @app.route('/')
    @cross_origin()
    def index():    
        return (""" Success! right on the API track sir :-) \
                Welcome to the worlds biggest music database.""")


    #  Records
    #----------------------------------------------------------------------------#

    @app.route('/records', methods=['GET'])
    @requires_auth('get:records')

    def records(payload):

        records = Record.query.order_by(Record.id).all()
        record_list = [record.format() for record in records]

        if records is None:
            abort(404)

        return jsonify({
            'success': True,
            'records': record_list,
            'code': 200
        })

    #----------------------------------------------------------------------------#

    @app.route('/records/<int:record_id>', methods=['GET'])
    @requires_auth('get:record-details')

    def show_record(payload, record_id):
    
        record = Record.query.filter_by(id=record_id).first()
    
        if record is None:
            abort(404)

        return jsonify({
            'success': True,
            'record': [record.format()],
            'code': 200
        })

    #----------------------------------------------------------------------------#
    
    @app.route('/records', methods=['POST'])
    @requires_auth('post:records')

    def post_record(payload):
        
        record = Record()
        
        for attribute, value in request.json.items():
            setattr(record, attribute, value)
        
        record.insert()
        
        return jsonify({
            'success': True,
            'record': [record.format()],
            'code': 200
        })

    #----------------------------------------------------------------------------#

    @app.route('/records/<int:record_id>', methods=['PATCH'])
    @requires_auth('patch:records')

    def patch_record(payload, record_id):
        
        record = Record.query.filter_by(id=record_id).first()
    
        if record == 0:
            abort(404)

        for attribute, value in request.json.items():
            setattr(record, attribute, value)
        
        record.update()
        
        return jsonify({
            'success': True,
            'record': record.format(),
            'code': 200
        })

    #----------------------------------------------------------------------------#

    @app.route('/records/<int:record_id>', methods=['DELETE'])
    @requires_auth('delete:records')

    def delete_record(payload, record_id):
        
        record = Record.query.filter_by(id=record_id).first()

        if record is None:
            abort(404)

        record.delete()

        return jsonify({
            'success': True,
            'record_id': record_id,
            'code': 200
        })
        

    #  Artists
    #----------------------------------------------------------------------------#

    @app.route('/artists', methods=['GET'])
    @requires_auth('get:artists')

    def artists(payload):

        artists = Artist.query.order_by(Artist.id).all()
        artist_list = [artist.format() for artist in artists]

        if artists is None:
            abort(404)

        return jsonify({
            'success': True,
            'artists': artist_list,
            'code': 200
        })

    #----------------------------------------------------------------------------#

    @app.route('/artists/<int:artist_id>', methods=['GET'])
    @requires_auth('get:artist-details')

    def show_artist(payload, artist_id):
    
        artist = Artist.query.filter_by(id=artist_id).first()
    
        if artist is None:
            abort(404)

        return jsonify({
            'success': True,
            'artist': [artist.format()],
            'code': 200
        })

    #----------------------------------------------------------------------------#
    
    @app.route('/artists', methods=['POST'])
    @requires_auth('post:artists')

    def post_artist(payload):
        
        artist = Artist()
        
        for attribute, value in request.json.items():
            setattr(artist, attribute, value)
        
        artist.insert()
        
        return jsonify({
            'success': True,
            'artist': [artist.format()],
            'code': 200
        })

    #----------------------------------------------------------------------------#

    @app.route('/artists/<int:artist_id>', methods=['PATCH'])
    @requires_auth('patch:artists')

    def patch_artist(payload, artist_id):
        
        artist = Artist.query.filter_by(id=artist_id).first()
    
        if artist == 0:
            abort(404)

        for attribute, value in request.json.items():
            setattr(artist, attribute, value)
        
        artist.update()
        
        return jsonify({
            'success': True,
            'artist': [artist.format()],
            'code': 200
        })

    #----------------------------------------------------------------------------#

    @app.route('/artists/<int:artist_id>', methods=['DELETE'])
    @requires_auth('delete:artists')

    def delete_artist(payload, artist_id):
        
        artist = Artist.query.filter_by(id=artist_id).first()

        if artist is None:
            abort(404)

        artist.delete()

        return jsonify({
            'success': True,
            'artist_id': artist_id,
            'code': 200
        })
        

    # Errors
    #----------------------------------------------------------------------------#

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False, 
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
                        "success": False, 
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
                        "success": False, 
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    @app.errorhandler(500)
    def internel_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
            }), 500

    @app.errorhandler(AuthError)
    def unauthorized_error(error):
        return jsonify({
                        "success": False, 
                        "error": error.status_code,
                        "message": error.error
                        }), 401

    return app

app = create_app()

if __name__ == '__main__':
    app.run()

