from flask import request, render_template, redirect, flash, jsonify
from flask.views import MethodView
from src.db import *

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cursor:
            cursor.execute("select * from Restaurants")
            data = cursor.fetchall()
            return render_template("public/index.html", data=data)
    
    def post(self):
        id = request.form["id"]
        rating = request.form["rating"]
        name = request.form["name"]
        site = request.form["site"]
        email = request.form["email"]
        phone = request.form["phone"]
        street = request.form["street"]
        city = request.form["city"]
        state = request.form["state"]
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])

        data = (
            id, rating, name, site, email, phone, street, city, state, latitude, longitude
        )

        with mysql.cursor() as cursor:
            try:
                cursor.execute("insert into Restaurants values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
                cursor.connection.commit()
                flash("Successfully saved restaurant", "success")
            except:
                flash("Save error", "error")
            return redirect("/")

class DeleteRestaurantController(MethodView):
    def post(self, id):
        with mysql.cursor() as cursor:
            try:
                cursor.execute("delete from Restaurants where id = %s", (id,))
                cursor.connection.commit()
                flash("Successfully deleted restaurant", "success")
            except:
                flash("Update error", "error")
            return redirect('/')

class UpdateRestaurantController(MethodView):
    def get(self, id):
        with mysql.cursor() as cursor:
            cursor.execute("select * from Restaurants where id = %s", (id,))
            restaurant = cursor.fetchone()
            return render_template("public/update.html", restaurant=restaurant)
    
    def post(self, id):
        new_id = request.form["id"]
        rating = request.form["rating"]
        name = request.form["name"]
        site = request.form["site"]
        email = request.form["email"]
        phone = request.form["phone"]
        street = request.form["street"]
        city = request.form["city"]
        state = request.form["state"]
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])

        data = (
            new_id, rating, name, site, email, phone, street, city, state, latitude, longitude, id
        )

        with mysql.cursor() as cursor:
            try:
                cursor.execute(
                    "update Restaurants set id=%s, rating=%s, name=%s, site=%s, email=%s, phone=%s, street=%s, city=%s, state=%s, lat=%s, lng=%s where id=%s", data
                )
                cursor.connection.commit()
                flash("Successfully updated restaurant", "success")
            except:
                flash("Update error", "error")
            return redirect("/")
            
class StatisticsController(MethodView):
    def get(self):
        with mysql.cursor() as cursor:
            response = {}
            try:
                latitude = float(request.args.get("latitude"))
                longitude = float(request.args.get("longitude"))
                radius = float(request.args.get("radius"))
                cursor.execute(f"call nearby({latitude}, {longitude}, {radius})")
                result = cursor.fetchone()
            
                response["count"] = result[0]
                response["avg"] = float(result[1])
                response["std"] = result[2]

                return jsonify(response)
            except:
                return jsonify({"message": "there is not data"})
