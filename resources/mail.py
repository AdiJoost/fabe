from flask_restful import Resource, reqparse
from flask import make_response
import flask
from utils.MailBot import sendMail


class Mail(Resource):
    def post(self):
        parser = Mail.get_parser()
        data = parser.parse_args()
        mail_message = "From: " + data["name"] + "\nMail: " + data["email"] + "\nMessage:\n\n" + data["text"]
        try:
            sendMail(reciver="adis.coole.firma@gmail.com", text=mail_message, subject=data["subject"])
            return Mail.create_response({"message": "Deine Nachricht wurde gesendet."}, 200)
        except Exception as e:
            with open("/var/www/log/error.txt", "a", encoding="utf-8") as file:
                file.writelines(e.message + "\n\n")
            return Mail.create_response({"message": "Oopps, die Nachricht konnte nicht übermittelt werden. Probiere es später oder schreibe eine E-Mail an adis.coole.firma@gmail.com"}, 500)
        
        
    @classmethod
    def get_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("name",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        parser.add_argument("email",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        
        parser.add_argument("subject",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        parser.add_argument("text",
                            type=str,
                            required=True,
                            help="This field cannot be left blank")
        return parser
    
    @classmethod
    def create_response (cls, body, status):
        response = make_response(flask.jsonify(body), status)
        response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
        return response
