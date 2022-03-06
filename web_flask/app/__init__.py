import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
webapp = Flask(__name__)

# ip of cache for remote access
ip_addr = "http://34.203.97.82:5001"

from app import photos
from app import cache
from app import api
from app import main

from app.models import create_tables
from app.models import clear_storage

webapp.config['JSON_SORT_KEYS'] = False
webapp.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

clear_storage.clear_old_contents('app/static/pictures')

# connect to mysql
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ece17792022@127.0.0.1:3306/webapp_1'
webapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.app = webapp
db.init_app(webapp)
db.drop_all()
db.create_all()
