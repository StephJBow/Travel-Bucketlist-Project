from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from app import db

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route("/bucketlist")
def show_bucketlist():
    
    chile = Country(country_name = "Chile")
    india = Country(country_name = "India")
    italy = Country(country_name = "Italy")
    south_africa = Country(country_name = "South Africa")
    japan = Country(country_name = "Japan")

    db.session.add(chile)
    db.session.add(india)
    db.session.add(italy)
    db.session.add(south_africa)
    db.session.add(japan)
    db.session.commit()

    santiago = City(city_name = "Santiago", visited = True, country=chile)
    valparaiso = City(city_name = "Valparaiso", visited = False, country=chile)
    antofagasta = City(city_name = "Antofagasta", visited = False, country=chile)
    mumbai = City(city_name = "Mumbai", visited = False, country=india)
    jaipur = City(city_name = "jaipur", visited = False, country=india)
    rome = City(city_name = "Rome", visited = False, country=italy)
    venice = City(city_name = "Venice", visited = False, country=italy)
    florence = City(city_name = "Florence", visited = False, country=italy)

    db.session.add(santiago)
    db.session.add(valparaiso)
    db.session.add(antofagasta)
    db.session.add(mumbai)
    db.session.add(jaipur)
    db.session.add(rome)
    db.session.add(venice)
    db.session.add(florence)
    db.session.commit()

    return "First list done!"