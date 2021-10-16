from flask_restful import Resource, reqparse
from models.resume_model import ResumeModel
from flask import make_response
import flask

class _Resumes(Resource):
    def get(self):
        resumes = ResumeModel.get_all()
        return_value = {}
        for resume in resumes:
            return_value[resume.id] = resume.to_json()
        return Resume.create_response(return_value, 200)
    
    def post(self):
        pass
    
    def delete(self):
        pass
    
    def put(self):
        pass
            
        
 


class Resume(Resource):
    def get(self, _id):
        resume = ResumeModel.get_by_id(_id)
        if resume:
            body = resume.to_json()
            status = 200
        else:
            body = {"message": "No resume with given id found"}
            status = 404
        return Resume.create_response(body, status)
            
    
    def post(self, _id):
        pass
        
    
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
    
    