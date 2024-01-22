from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from services.city_services import handle_city_update
from app import db

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route("/cities")
def show_cities():
    all_countries = Country.query.all()
    all_cities = City.query.all()
    return render_template('cities.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/cities/visited")
def visited_cities():
    all_countries = Country.query.all()
    all_cities = City.query.all()
    return render_template('visited.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/cities/notyetvisited")
def not_visited_cities():
    all_countries = Country.query.all()
    all_cities = City.query.all()
    return render_template('not_visited.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/cities/new")
def add_to_cities():
    all_countries = Country.query.all()
    all_cities = City.query.all()    
    return render_template('new.jinja', countries = all_countries, cities = all_cities)

@city_blueprint.route("/cities/new", methods=["POST"])
def add_new_city():
    city_name = request.form["city_name"]
    image_url = request.form["image_url"]
    visited = "visited" in request.form
    country_id = request.form["country_id"]
    new_city = City(city_name=city_name, image_url=image_url, visited = visited, country_id=country_id)
    db.session.add(new_city)
    db.session.commit()
    return redirect ("/cities")

@city_blueprint.route("/cities/<int:id>")
def show_one_city(id):
    city_to_show = City.query.get(id)    
    return render_template("one_city.jinja", city=city_to_show)

@city_blueprint.route("/cities/<int:id>/edit")
def edit_city(id):
    city_to_edit = City.query.get(id)
    return render_template('update_city.jinja', city=city_to_edit)

@city_blueprint.route("/cities/<int:id>/edit", methods = ['POST'])
def update_city(id):
    city_to_update = City.query.get(id)
    city_to_update.country.country_name = request.form["country_name"]
    city_to_update.city_name = request.form["city_name"]
    city_to_update.image_url = request.form["image_url"]
    
    if "visited" in request.form:
        city_to_update.visited = True
    else:
        city_to_update.visited = False
    db.session.commit()
    return redirect (f"/cities/{id}")

@city_blueprint.route("/cities/<int:id>/delete", methods= ['POST'])
def delete_city(id):
    city_to_delete = City.query.get(id)
    db.session.delete(city_to_delete)
    db.session.commit()
    return redirect (f"/cities") 