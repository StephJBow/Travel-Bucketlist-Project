from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:password@localhost:5432/travel_bucketlist"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.city import City
from models.country import Country

@app.route("/")
def home():
    return "This is the home page - can be a blank page with a link"

from controllers.city_controller import city_blueprint
app.register_blueprint(city_blueprint)

from controllers.country_controller import country_blueprint
app.register_blueprint(country_blueprint)