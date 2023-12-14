from app import db 
from models.city import City

def handle_city_update(form, id):
    city_to_update = City.query.get(id)
    
    city_to_update.country.country_name = form["country_name"]
    city_to_update.city_name = form["city_name"]
    city_to_update.image_url = form["image_url"]

    if "visited" in form:
        city_to_update.visited = True
    else:
        city_to_update.visited = False
    
    db.session.commit()