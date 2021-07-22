import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Actor, Movie

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,PATCH')
        # print('after_request')
        return response

    def check(dt):
        if dt is None:
            return False

        return True

    @app.route('/')
    def get_greeting():
        excited = os.getenv('EXCITED', default=None)
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

    @app.route('/actors/<int:id>', methods=['PATCH'])
    def patch_actors_by_id(id):
        actor = None

        try:
            actor = Actor.query.filter_by(id=id).first()
            post_json = request.get_json()

            if post_json.get('name'):
                actor.name = post_json.get('name')
            if post_json.get('age'):
                actor.age = post_json.get('age')
            if post_json.get('gender'):
                actor.gender = post_json.get('gender')
            if post_json.get('description'):
                actor.description = post_json.get('description')

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

    @app.route('/movies', methods=['POST'])
    def post_movies():
        post_json = request.get_json()
        title = post_json.get('title')
        released_date = post_json.get('released_date')
        genre = post_json.get('genre')
        description = post_json.get('description')

        if ((title is None)
            or (released_date is None)
            or (genre is None)
            or (description is None)):
            abort(422)

        try:
            movie = Movie(
                title, released_date, genre, description=description)
            movie.insert()

        except Exception as e:
            print(e)
            abort(422)

        return jsonify({
            'success': True,
            'movie_id': movie.id
        })

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = None

        try:
            movies = Movie.query.all()
        except Exception as e:
            print(e)
            abort(404)

        if check(movies) is False:
            abort(404)

        ds = [mv.get_as_json() for mv in movies]

        return jsonify({
            'success': True,
            'actors': ds
        })

    @app.route('/movies/<int:id>', methods=['GET'])
    def get_movies_by_id(id):
        movie = None

        try:
            movie = Movie.query.filter_by(id=id).first()
        except Exception as e:
            print(e)
            abort(404)

        if check(movie) is False:
            abort(404)

        return jsonify({
            'success': True,
            'actor': movie.get_as_json()
        })

    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movies_by_id(id):
        movie = None

        try:
            movie = Movie.query.filter_by(id=id).first()
            movie.delete()
        except Exception as e:
            print(e)
            abort(404)

        if check(movie) is False:
            abort(404)

        return jsonify({
            'success': True,
            'actor': movie.id
        })

    @app.route('/movies/<int:id>', methods=['PATCH'])
    def patch_movies_by_id(id):
        movie = None

        try:
            movie = Movie.query.filter_by(id=id).first()

            post_json = request.get_json()

            if post_json.get('title'):
                movie.title = post_json.get('title')
            if post_json.get('released_date'):
                movie.released_date = post_json.get('released_date')
            if post_json.get('genre'):
                movie.genre = post_json.get('genre')
            if post_json.get('description'):
                movie.description = post_json.get('description')

            movie.update()
        except Exception as e:
            print(e)
            abort(404)

        if check(movie) is False:
            abort(404)

        return jsonify({
            'success': True,
            'movie': movie.id
        })

    return app

application = create_app()

if __name__ == '__main__':
    port = os.getenv('PORT', default=9050)
    application.run(host='0.0.0.0', port=port)
