from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.target_model import TargetModel
from flask import make_response
import flask
import math

class Targets(Resource):
    def get(self):
        targets = TargetModel.get_all_targets()
        return_value = {}
        for target in targets:
            return_value[target.id] = target.to_json()
        return Target.create_response(return_value, 200)
    
    def post(self):
        parser = Targets.get_parser()
        data = parser.parse_args()
        input_code = data["types"]
        if (input_code == ""):
            return Target.create_response({}, 200)
        return_value = {}
        for i in range(len(input_code)):
            if(input_code[i] == "1"):
                targets = TargetModel.get_by_first_number(i + 1)
                for target in targets:
                    return_value[target.id] = target.to_json()
        return Target.create_response(return_value, 200)
            
        
    @classmethod
    def get_length(cls, number):
        return int(math.log10(number)) + 1
        
    @classmethod
    def get_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("types",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        return parser


class Target(Resource):
    def get(self, _id):
        target = TargetModel.get_by_id(_id)
        if target:
            status = 200
            body = target.to_json()
        else:
            status = 404
            body= {"message" : "Target not found"}
        return Target.create_response(body, status)
            
    
    def post(self, _id):
        parser = Target.get_post_parser()
        data = parser.parse_args()
        target = TargetModel(**data)
        target.save()
        status = 201
        body = {"message" : "Target created"}
        return Target.create_response(body, status)
    
    def delete (self, _id):
        target = TargetModel.get_by_id(_id)
        target.deleteMe()
        return Target.create_response({"message": "Item with that ID does not exist anymore"}, 200)
    
    def put(self, _id):
        parser = Target.get_put_parser()
        data = parser.parse_args()
        target = TargetModel.get_by_id(_id)
        if not target:
            return Target.create_response({"message": "Item with id does not exist. Put method won't create new item. Use Post method instead"})
        if data["name"] != None:
            target.name = data["name"]
        if data["description"]:
            target.description = data["description"]
        if data["target_type"]:
            target.target_type = data["target_type"]
        if data["first_number"]:
            target.first_number = data["first_number"]
        if data["second_number"]:
            target.second_number = data["second_number"]
        if data["third_number"]:
            target.third_number = data["third_number"]
        target.save()
        return Target.create_response({"message": "Target updated"}, 200)
        
    
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
        parser.add_argument("description",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        parser.add_argument("target_type",
                            type=str,
                            required=True,
                            help="This field cannot be left blank. Formmat: yyyy-MM-dd")
        parser.add_argument("first_number",
                            type=int,
                            required=True,
                            help="This field cannot be left blank.")
        parser.add_argument("second_number",
                            type=int,
                            required=True,
                            help="This field cannot be left blank.")
        parser.add_argument("third_number",
                            type=int,
                            required=True,
                            help="This field cannot be left blank.")
        
        return parser
    
    @classmethod
    def get_put_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("name",
                            type=str)
        parser.add_argument("description",
                            type=str,
                            required=True)
        parser.add_argument("target_type",
                            type=str)
        parser.add_argument("first_number",
                            type=int)
        parser.add_argument("second_number",
                            type=int)
        parser.add_argument("third_number",
                            type=int)
        return parser