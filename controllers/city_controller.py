from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from services.city_services import handle_city_update
from app import db

city_blueprint = Blueprint("cities", __name__)

# as mentioned prevously you should try and follow the restufl routing convetions naming your endpoints. here is a nice guide on the matter : https://restfulapi.net/resource-naming/
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
# we can consider extracting out logic and extra verbosity from our controller functions, we care more about _what_ are code is doing as opposed to _how_ its doing it. 
# see below for example
# this has the following benefits ..

# 1. Separation of concerns
# One of the core principles of software engineering is the separation of concerns. By moving business logic out of controllers and into separate components, you ensure that each component has a single responsibility. Controllers should primarily handle user input and orchestrate the flow of data, while logic related to data manipulation, validation, and business rules should be handled by other parts of the application.
# 2. Code Reusability (keeps us DRY)
# Extracting logic into separate modules or classes makes it more reusable. You can use the same logic in multiple controllers or even in different parts of your application. This reduces code duplication and leads to a more maintainable codebase.
# 3. Scalable 
# As your application grows, you may need to change or extend its functionality, if we have to do the same action several times, it helps if we have the logic to do that action central to one place if we suddenly need to change how we are doing that action we now need to just change the code in one place as apposed to every place we where doing that action.
# 4. Readability 
# Controllers are typically responsible for managing the flow of requests and responses. When logic is mixed with controller code, it can make controllers bulky and less readable. Extracting logic into separate files/folders leads to cleaner, more focused, and more readable code. This improves the overall maintainability of the application.
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

##############################
# example of code after extracting out logic
##############################
@city_blueprint.route("/bucketlist/<int:id>/edit", methods = ['POST'])
def update_destination(id):
    handle_city_update(request.form, id)
    return redirect (f"/bucketlist/{id}")




@city_blueprint.route("/bucketlist/<int:id>/delete", methods= ['POST'])
def delete_destination(id):
    city_to_delete = City.query.get(id)
    db.session.delete(city_to_delete)
    db.session.commit()
    return redirect (f"/bucketlist/{id}") 


# should tidy the below up

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