from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from app import db
# requests to do with 'countries' should be in this file
country_blueprint = Blueprint("countries", __name__)