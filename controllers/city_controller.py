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

@city_blueprint.route("/bucketlist/visited")
def visited_destinations():
    all_countries = Country.query.all()
    all_cities = City.query.all()
    return render_template('visited.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/bucketlist/notyetvisited")
def not_visited_destinations():
    all_countries = Country.query.all()
    all_cities = City.query.all()
    return render_template('not_visited.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/bucketlist/new")
def add_to_bucketlist():
    all_countries = Country.query.all()
    all_cities = City.query.all()    
    return render_template('new.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/bucketlist/new", methods=["POST"])
def add_new_city():
    city_name = request.form["city_name"]
    image_url = request.form["image_url"]
    visited = "visited" in request.form
    country_id = request.form["country_id"]
    new_city = City(city_name=city_name, image_url=image_url, visited = visited, country_id=country_id)
    db.session.add(new_city)
    db.session.commit()
    return redirect ("/bucketlist")

@city_blueprint.route("/bucketlist/new/country", methods=["POST"])
def add_new_country():
    country_name = request.form["country_name"]
    new_country = Country(country_name = country_name)
    db.session.add(new_country)
    db.session.commit()
    return redirect ("/bucketlist/new")

@city_blueprint.route("/bucketlist/<int:id>")
def show_one_destination(id):
    destination_city_to_show = City.query.get(id)    
    return render_template("one_destination.jinja", city=destination_city_to_show)

@city_blueprint.route("/bucketlist/<int:id>/edit")
def edit_bucketlist(id):
    destination_to_edit = City.query.get(id)
    return render_template('update_destination.jinja', city=destination_to_edit)

@city_blueprint.route("/bucketlist/<int:id>/edit", methods = ['POST'])
def update_destination(id):
    city_to_update = City.query.get(id)
    city_to_update.country.country_name = request.form["country_name"]
    city_to_update.city_name = request.form["city_name"]
    city_to_update.image_url = request.form["image_url"]
    
    if "visited" in request.form:
        city_to_update.visited = True
    else:
        city_to_update.visited = False
    db.session.commit()
    return redirect (f"/bucketlist/{id}")

@city_blueprint.route("/bucketlist/<int:id>/delete", methods= ['POST'])
def delete_destination(id):
    city_to_delete = City.query.get(id)
    db.session.delete(city_to_delete)
    db.session.commit()
    return redirect (f"/bucketlist/{id}") 


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

# santiago = City(city_name = "Santiago", visited = True, description = "put description here", image_url=".", country=chile)
# valparaiso = City(city_name = "Valparaiso", visited = False, description = "put description here", image_url=".", country=chile)
# antofagasta = City(city_name = "Antofagasta", visited = False, description = "put description here", image_url=".", country=chile)
# mumbai = City(city_name = "Mumbai", visited = False, description = "put description here", image_url=".", country=india)
# jaipur = City(city_name = "jaipur", visited = False, description = "put description here", image_url=".", country=india)
# rome = City(city_name = "Rome", visited = False, description = "put description here", image_url=".", country=italy)
# venice = City(city_name = "Venice", visited = False, description = "put description here", image_url=".", country=italy)
# florence = City(city_name = "Florence", visited = False, description = "put description here", image_url=".", country=italy)

# db.session.add(santiago)
# db.session.add(valparaiso)
# db.session.add(antofagasta)
# db.session.add(mumbai)
# db.session.add(jaipur)
# db.session.add(rome)
# db.session.add(venice)
# db.session.add(florence)
# db.session.commit()