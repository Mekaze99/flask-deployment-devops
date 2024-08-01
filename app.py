from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from prometheus_flask_exporter import PrometheusMetrics
from dotenv import load_dotenv
import os 

load_dotenv()

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

metrics = PrometheusMetrics(app)

class Base(DeclarativeBase):
  pass

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    country = db.Column(db.String(120), nullable=False)

@app.route("/")
def hello_world():
    return "<a href='/meals'>Potrawy tutaj byku!</a>"
  
@app.route("/meals", methods=["POST"])
def add_meal():
    if request.is_json:
        data = request.json
    else:
        data = request.form
    new_meal = Meals(name=data['name'], country=data['country'])
    db.session.add(new_meal)
    db.session.commit()
    return jsonify({"message": "Meal added"}), 201

@app.route("/meals", methods=["GET"])
def meals():
    if request.method == "POST":
        if request.is_json:
            data = request.json
        else:
            data = request.form
        new_meal = Meals(name=data['name'], country=data['country'])
        db.session.add(new_meal)
        db.session.commit()
        return jsonify({"message": "Meal added"}), 201

    meals = Meals.query.all()
    meals_list = [{"id": meal.id, "name": meal.name, "country": meal.country} for meal in meals]
    return render_template("meals.html", meals=meals_list)

if __name__ == "__main__":
    app.run(debug=True)
