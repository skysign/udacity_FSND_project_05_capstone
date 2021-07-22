import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    def check(dt):
        if dt is None:
            return False

        return True

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = None

        try:
            actors = Actors.query.all()
        except Exception as e:
            print(e)
            abort(404)

        if check(drinks) is False:
            abort(404)

        ds = [ac.get_as_json() for ac in actors]

        return jsonify({
            'success': True,
            'actors': ds
        })

    @app.route('/actors/<int:id>', methods=['GET'])
    def get_actor_id(id):
        actor = None

        try:
            actor = Actors.query.filter_by(id=id).first()
        except Exception as e:
            print(e)
            abort(404)

        if check(actor) is False:
            abort(404)

        return jsonify({
            'success': True,
            'actor': actor.get_as_json()
        })

    @app.route('/actors', methods=['POST'])
    def post_actors():
        post_json = request.get_json()

        name = post_json.get('name')
        age = post_json.get('age')
        gender = post_json.get('gender')
        description = post_json.get('description')

        if ((name is None)
            or (age is None)
            or (gender is None)
            or (description is None)):
            abort(422)

        try:
            actor = Actors(
                name, age, gender, description=description)
            actor.insert()

        except Exception as e:
            print(e)
            abort(422)

        return jsonify({
            'success': True,
            'actor_id': actor_id
        })

    return app

application = create_app()

if __name__ == '__main__':
    application.run()
