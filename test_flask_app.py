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

    def tearDown(self):
        """Executed after reach test"""
        pass

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


    # def test_search_questions(self):
    #     response = self.client().post('/questions',
    #                                   json={'searchTerm': 'boxer'})
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(len(data['questions']), 1)
    #     self.assertEqual(data['questions'][0]['id'], 9)
    #     self.assertEqual(
    #         data['questions'][0]['question'],
    #         'What boxer\'s original name is Cassius Clay?')
    #
    # def test_post_new_questions(self):
    #     response = self.client().post('/questions', json=self.new_question)
    #     data = json.loads(response.data)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(data['created'])
    #
    #     question = Question.query.filter_by(id=data['created']).first()
    #     question.delete()
    #
    # def test_delete_question(self):
    #     # To test 'delete', we insert a question to delete
    #     question = Question(
    #         question=self.new_question['question'],
    #         answer=self.new_question['answer'],
    #         category=self.new_question['category'],
    #         difficulty=self.new_question['difficulty'])
    #     question.insert()
    #
    #     response = self.client().delete('/questions/{}'.format(question.id))
    #     data = json.loads(response.data)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], question.id)
    #
    # def test_category_questions(self):
    #     response = self.client().get('/categories/1/questions')
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['current_category'])
    #
    # def test_play_quiz_game(self):
    #     response = self.client().post('/quizzes',
    #                                   json={'previous_questions': [2, 6],
    #                                         'quiz_category': {
    #                                             'type': 'Entertainment',
    #                                             'id': '5'}})
    #     data = json.loads(response.data)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['question'])
    #     self.assertEqual(data['question']['category'], 5)
    #     self.assertNotEqual(data['question']['id'], 2)
    #     self.assertNotEqual(data['question']['id'], 6)
    #
    # def test_play_quiz_fails(self):
    #     response = self.client().post('/quizzes', json={})
    #
    #     data = json.loads(response.data)
    #
    #     self.assertEqual(response.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Unprocessable Entity')
    #
    # def test_404_request(self):
    #     # send request with bad page data, load response
    #     response = self.client().get('/questions?page=10000')
    #     data = json.loads(response.data)
    #
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not Found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
