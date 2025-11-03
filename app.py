from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os


from models import db
from routes.users import users

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(users, url_prefix='/users')

with app.app_context():
    db.create_all()   # This will check all models and create missing tables

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)