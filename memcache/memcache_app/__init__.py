import imp
from flask import Flask
from memcache_app.memcache import Memcache
from flask_sqlalchemy import SQLAlchemy

webapp = Flask(__name__)
db = SQLAlchemy()
memcache = Memcache()

from memcache_app import main
from memcache_app.models import create_tables
from memcache_app.timer import send_statistics

webapp.config['JSON_SORT_KEYS'] = False
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ece17792022@127.0.0.1:3306/webapp_1'
webapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.app = webapp
db.init_app(webapp)
# db.drop_all()
# db.create_all()

send_statistics()