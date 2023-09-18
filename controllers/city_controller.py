from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from app import db

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route("/bucketlist")
def show_bucketlist():
    all_countries = Country.query.all()
    all_cities = City.query.all()
    return render_template('bucketlist.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/bucketlist/new")
def add_to_bucketlist():
    all_countries = Country.query.all()
    all_cities = City.query.all()    
    return render_template('new.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/bucketlist/new", methods=["POST"])
def add_new_city():
    new_city_name = request.form["city_name"]
    new_country_id = request.form["countries"]
    new_city = City(city_name=new_city_name, country_id=new_country_id)
    db.session.add(new_city)
    db.session.commit()
    return redirect ("/bucketlist")

@city_blueprint.route("/bucketlist/<id>/<city_id>")
def show_one_destination(id, city_id):
    destination_country_to_show = Country.query.get(id)
    destination_city_to_show = City.query.get(city_id)    
    return render_template("one_destination.jinja", country=destination_country_to_show, city=destination_city_to_show)

@city_blueprint.route("/bucketlist/<id>/<city_id>/edit")
def edit_bucketlist(id, city_id):
    destination_to_edit = City.query.get(city_id)
    destination_country = Country.query.get(id)
    return render_template('update_destination.jinja', city=destination_to_edit, country = destination_country)

@city_blueprint.route("/bucketlist/<id>/<city_id>/edit", methods = ['POST'])
def update_destination(id, city_id):
    city_to_update = City.query.get(city_id)
    city_to_update.country_of_city = Country.query.get(id)
    city_to_update.country.country_name = request.form["country_name"]
    city_to_update.city.city_name = request.form["city_name"]
    city_to_update.city.visited = request.form["visited"]
    db.session.commit()
    return redirect ("/bucketlist")


    # chile = Country(country_name = "Chile")
    # india = Country(country_name = "India")
    # italy = Country(country_name = "Italy")
    # south_africa = Country(country_name = "South Africa")
    # japan = Country(country_name = "Japan")

    # db.session.add(chile)
    # db.session.add(india)
    # db.session.add(italy)
    # db.session.add(south_africa)
    # db.session.add(japan)
    # db.session.commit()

    # santiago = City(city_name = "Santiago", visited = True, country=chile)
    # valparaiso = City(city_name = "Valparaiso", visited = False, country=chile)
    # antofagasta = City(city_name = "Antofagasta", visited = False, country=chile)
    # mumbai = City(city_name = "Mumbai", visited = False, country=india)
    # jaipur = City(city_name = "jaipur", visited = False, country=india)
    # rome = City(city_name = "Rome", visited = False, country=italy)
    # venice = City(city_name = "Venice", visited = False, country=italy)
    # florence = City(city_name = "Florence", visited = False, country=italy)

    # db.session.add(santiago)
    # db.session.add(valparaiso)
    # db.session.add(antofagasta)
    # db.session.add(mumbai)
    # db.session.add(jaipur)
    # db.session.add(rome)
    # db.session.add(venice)
    # db.session.add(florence)
    # db.session.commit()

    # return "First list done!"