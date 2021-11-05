from src.controllers.controller import *

routes = {
    "index-route": "/", "index-controller": IndexController.as_view("index"),
    "delete-route": "/delete/restaurant/<string:id>", "delete-controller": DeleteRestaurantController.as_view("delete"),
    "update-route": "/update/restaurant/<string:id>", "update-controller": UpdateRestaurantController.as_view("update"),
    "statistics-route": "/restaurants/statistics", "statistics-controller": StatisticsController.as_view("statistics")
}