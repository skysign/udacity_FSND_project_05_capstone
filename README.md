# Motivation of Project
This is the last project of Udacity Full Stack Web Developer Nanodegree (nd0044 v2),
to implement a set of specified endpoints by using flask.
auth0.com will be used for authentication and authorization, also.
And project will be hosted in heroku to demonstrate RESTfull APIs.

* Project 05 capstone in Udacity Full Stack Web Developer Nanodegree (nd0044 v2)
* Author: skysign@gmail.com

# Getting Started
* Recommended to use virtualenv to avoid any conflict in other existed flask app.
```
python -m venv venv
venv/bin/activate
```
* Please use the command below to install dependent libs at once
```
pip3 install -r requirements.txt
```
* To create tables from Models, please initialize 'flask db'
```
flask db init
flask db migrate -m "Migration :-)"
flask db upgrade
```
* In order to run the server of RESTfull APIs, please do below. This project is available to be hosted at heroku, also.
```
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=9050
export AUTH0_DOMAIN={YOUR_DOMAIN}.auth0.com
export ALGORITHMS={ALGORITHMS}
export API_AUDIENCE={AUDIENCE}
export DATABASE_URL="postgresql://{USER}:{PASSWORD}@127.0.0.1:5432/db_fsnd_project_05"
export PORT=9050
export EXCITED=true
flask run
```
* To verify RESTfull APIs locally, please run like below
  * Before running below, please set DATABASE_URL correctly.
```
python test_flask_app.py
```
* Please visit below to see running RESTfull APIs
  * https://udacity-fsnd-project-05.herokuapp.com/

# Specifications
## General Specifications
* Models will include at least…
  * Two classes with primary keys at at least two attributes each
  * [Optional but encouraged] One-to-many or many-to-many relationships between classes
* Endpoints will include at least…
  * Two GET requests
  * One POST request
  * One PATCH request
  * One DELETE request
    Roles will include at least…
  * Two roles with different permissions
  * Permissions specified for all endpoints
    Tests will include at least….
  * One test for success behavior of each endpoint
  * One test for error behavior of each endpoint
  * At least two tests of RBAC for each role

## Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

* Models:
  * Movies with attributes title and release date
  * Actors with attributes name, age and gender

* Roles:
  * Casting Assistant
    * Can view actors and movies
    * Has `get:actors, get:actors_id, get:movies, get:movies_id` permissions
  * Casting Director
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database
    * Modify actors or movies
    * Has all of permissions of Casting Assistant, also
    * Has `patch:actors, patch:movies, post:actors, post:movies` permissions
  * Executive Producer
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database
    * Has `delete:actors, delete:movies` permissions
    * Has all of permissions of Casting Director
* Tests:
  * One test for success behavior of each endpoint
  * One test for error behavior of each endpoint
  * At least two tests of RBAC for each role

# Endpoints
The endpoints below are provided.
  * GET /actors and /movies
  * DELETE /actors/ and /movies/
  * POST /actors and /movies
  * PATCH /actors/ and /movies/

 Please see below for more details.

## POST /actors
* Add new actor
* Required permission : `post:actors`
* Request detail
  `name`, `age`, `gender`, and `description` are needed, please see `sample POST request` below.
  * Sample POST request
```
  {
      "name": "actor_json_name",
      "age": 1,
      "gender": "female",
      "description": "actor_json_name age1 gender female"
  }
```

* Response detail
  * success: `True` if succeed, otherwise `False`
  * actor_id: Add actor's id

## GET /actors
* Return a list of actors
* Required permission : `get:actors`
* Response detail
  * success: `True` if succeed, otherwise `False`
  * actors: an whole list of actor as json
  * Sample response
```
    {
        "success": true
        "actors": [
            {
                "age": 1,
                "description": "actor_json_name age1 gender female",
                "gender": "female",
                "id": 137,
                "name": "actor_json_name"
            },
            {
                "age": 1,
                "description": "actor_json_name age1 gender female",
                "gender": "female",
                "id": 138,
                "name": "actor_json_name"
            },
            {
                "age": 1,
                "description": "actor_json_name age1 gender female",
                "gender": "female",
                "id": 187,
                "name": "actor_json_name"
            }
        ],
    }
```

## GET /actors/<int:id>
* Return a actor, pointed by id
* Required permission : `get:actors_id`
* Response detail
  * success: `True` if succeed, otherwise `False`
  * actor: actor as json format, pointed by id
  * Sample response
```
{
    "success": true
    "actor": {
        "age": 1,
        "description": "actor_json_name age1 gender female",
        "gender": "female",
        "id": 3,
        "name": "actor_json_name"
    },
}
```

## DELETE /actors/<int:id>
* Delete a actor, pointed by id
* Required permission : `delete:actors_id`
* Response detail
  * success: `True` if succeed, otherwise `False`
  * actor_id: deleted actor's id
  * Sample response
```
{
    "success": true
    "actor_id": 1
}
```

## PATCH /actors/<int:id>
* Update a actor, pointed by id
* Required permission : `patch:actors_id`
* Request detail
  `name`, `age`, `gender`, and `description` are needed, please see `sample POST request` below.
  * Sample POST request
```
  {
      "name": "actor_json_name",
      "age": 1,
      "gender": "female",
      "description": "actor_json_name age1 gender female"
  }
```
* Response detail
  * success: `True` if succeed, otherwise `False`
  * actor_id: updated actor's id
  * Sample response
```
{
    "success": true
    "actor_id": 1
}
```

## POST /movies
* Add new movie
* Required permission : `post:movies`
* Request detail
  `title`, `released_date`, `genre`, and `description` are needed, please see `Sample POST request` below.
  * Sample POST request
```
{
    'title': 'movie_title',
    'released_date': '2021-07-23',
    'genre': 'SF',
    'description': 'movie_title 2021-07-23 SF'
}
```
* Response detail
  * success: `True` if succeed, otherwise `False`
  * movie_id: deleted movie's id
  * Sample response
```
{
    "success": true
    "movie_id": 1
}
```

## GET /movies
* Return a list of movies
* Required permission : `get:movies`
* Response detail
  * success: `True` if succeed, otherwise `False`
  * movies: an whole list of actor as json
  ```
      {
          "success": true
          "movies": [
              {
                  "id": 137,
                  'title': 'movie_title',
                  'released_date': '2021-07-23',
                  'genre': 'SF',
                  'description': 'movie_title 2021-07-23 SF'
              },
              {
                  "id": 138,
                  'title': 'movie_title',
                  'released_date': '2021-07-23',
                  'genre': 'SF',
                  'description': 'movie_title 2021-07-23 SF'
              },
              {
                  "id": 139,
                  'title': 'movie_title',
                  'released_date': '2021-07-23',
                  'genre': 'SF',
                  'description': 'movie_title 2021-07-23 SF'
              }
          ],
      }
  ```

## GET /movies/<int:id>
* Return a movie, pointed by id
* Required permission : `get:movies_id`
* Response detail
  * success: `True` if succeed, otherwise `False`
  * movie: an whole list of actor as json
  ```
      {
          "success": true
          "movie": [
              {
                  "id": 137,
                  'title': 'movie_title',
                  'released_date': '2021-07-23',
                  'genre': 'SF',
                  'description': 'movie_title 2021-07-23 SF'
              }
          ],
      }
  ```

## DELETE /movies/<int:id>
* Delete a movie, pointed by id
* Required permission : `delete:movies_id`
* Response detail
  * success: `True` if succeed, otherwise `False`
  * movie_id: deleted movie's id
  * Sample response
```
{
    "success": true
    "movie_id": 1
}
```

## PATCH /movies/<int:id>
* Update a movie, pointed by id
* Required permission : `patch:movies_id`
* Request detail
  `title`, `released_date`, `genre`, and `description` are needed, please see `Sample POST request` below.
  * Sample POST request
```
{
    'title': 'movie_title',
    'released_date': '2021-07-23',
    'genre': 'SF',
    'description': 'description :) movie_title 2021-07-23 SF'
}
```
* Response detail
  * success: `True` if succeed, otherwise `False`
  * movie_id: updated movie's id
  * Sample response
```
{
    "success": true
    "movie_id": 1
}
```
