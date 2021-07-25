# Motivation of Project
This is the last project of Udacity Full Stack Web Developer Nanodegree (nd0044 v2),
to implement a set of specified endpoints by using flask.
auth0.com will be used for authentication and authorization, also.
And project will be hosted in heroku to demonstrate RESTfull APIs.

* Project 05 capstone in Udacity Full Stack Web Developer Nanodegree (nd0044 v2)
* Author: skysign@gmail.com

# Getting Started
* Recommended to use virtualenv to avoid any conflict in other existed flask app.
* Please use the command below to install dependent libs at once
```
pip install -r requirements.txt
```
* Please visit below to see running RESTfull APIs
  * https://udacity-fsnd-project-05.herokuapp.com/

* To verify RESTfull APIs locally, please run like below
  * Before running below, please set DATABASE_URL correctly.
```
python test_flask_app.py
```

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
  * Casting Director
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database
    * Modify actors or movies
  * Executive Producer
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database
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

## GET /actors
* Return a list of actors

## GET /actors/<int:id>
* Return a actor, pointed by id

## DELETE /actors/<int:id>
* Delete a actor, pointed by id

## PATCH /actors/<int:id>
* Update a actor, pointed by id

## POST /movies
* Add new movie

## GET /movies
* Return a list of movies

## GET /movies/<int:id>
* Return a movie, pointed by id

## DELETE /movies/<int:id>
* Delete a movie, pointed by id

## PATCH /movies/<int:id>
* Update a movie, pointed by id
