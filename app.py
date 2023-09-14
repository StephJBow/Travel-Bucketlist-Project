from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:password@localhost:5432/travel_bucketlist"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return "This is the home page!"