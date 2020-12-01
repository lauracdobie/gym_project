from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.class_type import ClassType
from models.member import Member
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def all_bookings():
    all_bookings = booking_repository.select_all()
    return render_template("bookings/all_bookings.html", all_bookings = all_bookings)

@bookings_blueprint.route("/bookings/book-class")
def booking_form():
    all_fitness_classes = fitness_class_repository.select_all()
    return render_template("/bookings/index.html", all_fitness_classes = all_fitness_classes)

# @bookings_blueprint.route("/bookings", methods=['POST'])
# def create_booking():
#     fitness_class = fitness_class_repository.select(request.form['fitness_class_id'])
#     member = member_repository.select_by_membership_no(request.form['membership_no'])
    
#     new_booking = Booking(member, fitness_class)
#     booking_repository.add(new_booking)
#     return redirect('/bookings')

@bookings_blueprint.route("/bookings/class-full")
def class_full_message():
    return render_template("bookings/class_full.html")

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    fitness_class = fitness_class_repository.select(request.form['fitness_class_id'])
    member = member_repository.select_by_membership_no(request.form['membership_no'])
    id = request.form['fitness_class_id']
    class_type = fitness_class.class_type
    date = fitness_class.date
    time = fitness_class.time
    duration = fitness_class.duration
    instructor = fitness_class.instructor
    location = fitness_class.location


    if fitness_class.capacity > 0:
        capacity = fitness_class.capacity - 1
        fitness_class = FitnessClass(class_type, date, time, duration, instructor, capacity, location, id)
        fitness_class_repository.edit(fitness_class)
        new_booking = Booking(member, fitness_class)
        booking_repository.add(new_booking)
        return redirect('/bookings')

    else:
        return redirect('/bookings/class-full')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking = booking_repository.select(id)
    fitness_class_id = booking.fitness_class.id
    fitness_class = fitness_class_repository.select(booking.fitness_class.id)
    class_type = fitness_class.class_type
    date = fitness_class.date
    time = fitness_class.time
    duration = fitness_class.duration
    instructor = fitness_class.instructor
    location = fitness_class.location
    capacity = fitness_class.capacity + 1

    fitness_class = FitnessClass(class_type, date, time, duration, instructor, capacity, location, fitness_class_id)
    fitness_class_repository.edit(fitness_class)
    
    booking_repository.delete(id)
    return redirect('/bookings')