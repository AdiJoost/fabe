from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.local_target import Target, Targets
from resources.local_theorie import Theorie, Theories
from db import db
import os.path


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

@app.route('/targets', methods=['GET'])
def targets_html():
    return render_template("targets.html")

@app.route('/models', methods=['GET'])
def models():
    return render_template("models.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/impressum', methods=['GET'])
def impressum():
    return render_template("impressum.html")

@app.route('/resumes', methods=['GET'])
def resumes():
    return render_template("resumes.html")

@app.route('/model/<string:html>')
def model(html):
    if os.path.isfile("templates/" + html):
        return render_template(html)
    else:
        return render_template("404.html")



api.add_resource(Target, '/target/<int:_id>')
api.add_resource(Targets, '/all_targets')
api.add_resource(Theorie, '/theorie/<int:_id>')
api.add_resource(Theories, '/theories')


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=4999, host="0.0.0.0", debug=True)