from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

db = SQLAlchemy()

migrate = Migrate(app, db)

db.init_app(app)

# flask db init - initialized our migration repository
# flask db migrate -m"detailed message of what has changed" - create a new migration
#                  compares what is in the models that are imported in app.py to what is in the database
#                  migration will contain how to update the database
# flask db upgrade - run the newest migration upgrade function