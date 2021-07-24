import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

class AppTestCase(unittest.TestCase):
    """This class represents the app test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = { 'name': 'actor_json_name',
                           'age': 1,
                           'gender': 'female',
                           'description': 'actor_json_name age1 gender female'
                         }

        self.new_movie = { 'title': 'movie_title',
                           'released_date': '2021-07-23',
                           'genre': 'SF',
                           'description': 'movie_title 2021-07-23 SF'
                         }

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''/actors test cases'''
    def test_post_actors(self):
        response = self.client().post('/actors', json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor_id'] > 0, True)

        # Removed an add actor by test_post_actors()
        actor = Actor.query.filter_by(id=data['actor_id']).first()
        actor.delete()

    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors_by_id(self):
        # Created an actor for testing test_delete_actors_by_id()
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'],
            description=self.new_actor['description'])
        actor.insert()

        response = self.client().get('/actors/{}'.format(actor.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['id'], actor.id)

        actor.delete()

    def test_delete_actors_by_id(self):
        # Created an actor for testing test_delete_actors_by_id()
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'],
            description=self.new_actor['description'])
        actor.insert()

        response = self.client().delete('/actors/{}'.format(actor.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor_id'] > 0, True)

    def test_patch_actors_by_id(self):
        # Created an actor for testing test_patch_actors_by_id()
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'],
            description=self.new_actor['description'])
        actor.insert()

        self.new_actor['description'] = 'patch ' + self.new_actor['description']

        response = self.client().patch('/actors/{}'.format(actor.id), json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor_id'] > 0, True)

        actor.delete()

    '''/movies test cases'''
    def test_post_movies(self):
        response = self.client().post('/movies', json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie_id'] > 0, True)

        # Removed an add actor by test_post_actors()
        movie = Movie.query.filter_by(id=data['movie_id']).first()
        movie.delete()

    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_by_id(self):
        # Created an movie for testing test_get_movies_by_id()
        movie = Movie(
            title=self.new_movie['title'],
            released_date=self.new_movie['released_date'],
            genre=self.new_movie['genre'],
            description=self.new_movie['description'])
        movie.insert()

        response = self.client().get('/movies/{}'.format(movie.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['id'], movie.id)

        movie.delete()

    def test_delete_movies_by_id(self):
        # Created a movie for testing test_delete_actors_by_id()
        movie = Movie(
            title=self.new_movie['title'],
            released_date=self.new_movie['released_date'],
            genre=self.new_movie['genre'],
            description=self.new_movie['description'])
        movie.insert()

        response = self.client().delete('/movies/{}'.format(movie.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie_id'], movie.id)

    def test_patch_movies_by_id(self):
        # Created a movie for testing test_patch_movies_by_id()
        movie = Movie(
            title=self.new_movie['title'],
            released_date=self.new_movie['released_date'],
            genre=self.new_movie['genre'],
            description=self.new_movie['description'])
        movie.insert()

        self.new_movie['description'] = 'patch ' + self.new_movie['description']

        response = self.client().patch('/movies/{}'.format(movie.id), json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie_id'], movie.id)

        movie.delete()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
