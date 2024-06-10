#!/usr/bin/env python3

from models import db, Scientist, Mission, Planet
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Scientists(Resource):
    def get(self):
        scientists = []
        for scientist in Scientist.query.all():
            scientists.append(scientist.to_dict(rules=('-missions',)))
        return make_response(scientists)

    def post(self):
        params = request.json
        try:
            scientist = Scientist(name=params.get('name'), field_of_study=params.get('field_of_study'))
            db.session.add(scientist)
            db.session.commit()
            return make_response(scientist.to_dict())
        except ValueError as v_error:
            # return make_response({'errors': [str(v_error)]}, 400)
            return make_response({'errors': ["validation errors"]}, 400)

api.add_resource(Scientists, '/scientists')

class ScientistById(Resource):
    def get(self, id):
        scientist = db.session.get(Scientist, id)
        if not scientist:
            return make_response({"error": "Scientist not found"}, 404)
        return make_response(scientist.to_dict())

    def patch(self, id):
        scientist = db.session.get(Scientist, id)
        if not scientist:
            return make_response({"error": "Scientist not found"}, 404)
        
        try:
            params = request.json
            for attr in params:
                setattr(scientist, attr, params[attr])
            db.session.commit()
            return make_response(scientist.to_dict(), 202)
        except ValueError as v_error:
            # return make_response({'errors': [str(v_error)]}, 400)
            return make_response({'errors': ["validation errors"]}, 400)

    def delete(self, id):
        scientist = db.session.get(Scientist, id)
        if not scientist:
            return make_response({"error": "Scientist not found"}, 404)
        
        db.session.delete(scientist)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(ScientistById, '/scientists/<int:id>')

class Planets(Resource):
    def get(self):
        planets = [planet.to_dict() for planet in Planet.query.all()]
        return make_response(planets)

api.add_resource(Planets, '/planets')

class Missions(Resource):
    def post(self):
        params = request.json
        try:
            mission = Mission(name=params.get('name'), scientist_id=params.get('scientist_id'), planet_id=params.get('planet_id'))
            db.session.add(mission)
            db.session.commit()
            return make_response(mission.to_dict(), 201)
        except ValueError as v_error:
            # return make_response({'errors': [str(v_error)]}, 400)
            return make_response({'errors': ["validation errors"]}, 400)

api.add_resource(Missions, '/missions')

@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
