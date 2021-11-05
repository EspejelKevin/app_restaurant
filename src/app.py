from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='development'
)

app.add_url_rule(routes["index-route"], view_func=routes["index-controller"])
app.add_url_rule(routes["delete-route"], view_func=routes["delete-controller"])
app.add_url_rule(routes["update-route"], view_func=routes["update-controller"])
app.add_url_rule(routes["statistics-route"], view_func=routes["statistics-controller"])