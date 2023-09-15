from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
from app import db

country_blueprint = Blueprint("countries", __name__)