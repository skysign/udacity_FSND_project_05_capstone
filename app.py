import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Actor, Movie

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,PATCH')
        return response

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
            actors = Actor.query.all()
        except Exception as e:
            print(e)
            abort(404)

        if check(actors) is False:
            abort(404)

        ds = [ac.get_as_json() for ac in actors]

        return jsonify({
            'success': True,
            'actors': ds
        })

    @app.route('/actors/<int:id>', methods=['GET'])
    def get_actors_by_id(id):
        actor = None

        try:
            actor = Actor.query.filter_by(id=id).first()
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
            actor = Actor(
                name, age, gender, description=description)
            actor.insert()

        except Exception as e:
            print(e)
            abort(422)

        return jsonify({
            'success': True,
            'actor_id': actor.id
        })

    return app

    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actors_by_id(id):
        actor = None

        try:
            actor = Actor.query.filter_by(id=id).first()
            actor.delete()
        except Exception as e:
            print(e)
            abort(404)

        if check(actor) is False:
            abort(404)

        return jsonify({
            'success': True,
            'actor': actor.id
        })

    @app.route('/actors/<int:id>', methods=['PATCH'])
    def patch_actors_by_id(id):
        actor = None
        post_json = request.get_json()

        try:
            actor = Actor.query.filter_by(id=id).first()

            post_json = request.get_json()

            if post_json.get('name'):
                name = post_json.get('name')
            if post_json.get('age'):
                age = post_json.get('age')
            if post_json.get('gender'):
                gender = post_json.get('gender')
            if post_json.get('description'):
                description = post_json.get('description')

            actor.update()
        except Exception as e:
            print(e)
            abort(404)

        if check(actor) is False:
            abort(404)

        return jsonify({
            'success': True,
            'actor': actor.id
        })

application = create_app()

if __name__ == '__main__':
    application.run()
