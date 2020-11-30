from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.class_type import ClassType
from models.member import Member
from models.booking import Booking
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/book-class")
def booking_form():
    return render_template("bookings/index.html")

# @bookings_blueprint.route("/book-class", methods=['POST'])
# def create_booking():
#     fitness_class = fitness_class_repository.select(request.form['fitness_class_id'])
#     date = request.form['date']
#     time = request.form['time']
#     duration = request.form['duration']
#     instructor = request.form['instructor']
#     location = request.form['location']
#     capacity = request.form['capacity']

#     print("🐰" + class_type.name + "🐰")

#     new_class = FitnessClass(class_type, date, time, duration, instructor, capacity, location)
#     fitness_class_repository.add(new_class)
#     return redirect('/fitness-classes')