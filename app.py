from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "LolHAHAHA"
api = Api(app)

jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_table():
    db.create_all()
    
    
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")




if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, host="0.0.0.0", debug=True)
