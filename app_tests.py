import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv(verbose=False)
from app import create_app
from models import setup_db, Record, Artist


class ApiTestCase(unittest.TestCase):
    """This class represents the api test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.token_manager = os.getenv('TOKEN_MANAGER')   
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "wmd_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', '','localhost:5432', self.database_name)
        #self.headers = {'Authorization': f'Bearer {os.getenv("TOKEN_MANAGER")}'}
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_records(self):
        res = self.client().get('/records', headers={
            "Authorization": 'bearer '+self.token_manager})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
   
    def test_records_error_no_header(self):
        res = self.client().get('/records')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        
    def test_artists(self):
        res = self.client().get('/artists', headers={
            "Authorization": 'bearer '+self.token_manager} )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_records_id(self):
        res = self.client().get('/records/5', headers={
            "Authorization": 'bearer '+self.token_manager}) # check that record with id=5 exists
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200) 

    def test_artists_id(self):
        res = self.client().get('/artists/5', headers={
            "Authorization": 'bearer '+self.token_manager}) # check that record with id=5 exists
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)


# # #  Errors
# # #----------------------------------------------------------------------------#
            
    def test_delete_record_error_404(self):      
        res = self.client().delete('/records/500', headers={
            "Authorization": 'bearer '+self.token_manager})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_delete_artist_error_404(self):      
        res = self.client().delete('/artists/500', headers={
            "Authorization": 'bearer '+self.token_manager})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()