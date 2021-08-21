from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.theorie_model import TheorieModel
from flask import make_response
import flask

class Theories(Resource):
    def get(self):
        pass
    
    def post(self):
        pass
            
        
 


class Theorie(Resource):
    def get(self, _id):
        theorie = TheorieModel.get_by_id(_id)
        if theorie:
            body = theorie.to_json()
            status = 200
        else:
            body = {"message": "No theorie with given id found"}
            status = 404
        return Theorie.create_response(body, status)
            
    
    def post(self, _id):
        parser = Theorie.get_post_parser()
        data = parser.parse_args()
        theorie = TheorieModel(**data)
        theorie.save()
        return Theorie.create_response({"message": "Theorie created"}, 201)
        
    
    def delete (self, _id):
        pass
    
    def put(self, _id):
        pass
        
    
    @classmethod
    def create_response (cls, body, status):
        response = make_response(flask.jsonify(body), status)
        response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
        return response
    
    @classmethod
    def get_post_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("name",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        parser.add_argument("html",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        parser.add_argument("picture",
                            type=str,
                            required=True,
                            help="This field cannot be left blank.")
        return parser
    
    @classmethod
    def get_put_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("name",
                            type=str)
        parser.add_argument("html",
                            type=str,
                            required=True)
        parser.add_argument("picture",
                            type=str)
        return parser