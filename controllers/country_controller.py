from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from app import db

country_blueprint = Blueprint("countries", __name__)

@country_blueprint.route("/cities/new/country", methods=["POST"])
def add_new_country():
    country_name = request.form["country_name"]
    new_country = Country(country_name = country_name)
    db.session.add(new_country)
    db.session.commit()
    return redirect ("/cities/new")