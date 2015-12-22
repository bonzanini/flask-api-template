Minimal Flask App
=================

Basic template to develop an API with Flask, Flask-RESTful and
Flask-RESTful-Swagger

Usage
-----

Clone the repo:

    git clone https://github.com/bonzanini/flask-api-template
    cd flask-api-template

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py develop # or install if you prefer

Run the sample server

    python runserver.py

Try the endpoints:

    curl -XGET http://localhost:5000/dummy
    curl -XPOST http://localhost:5000/hello -d '{"name": "World"}'


