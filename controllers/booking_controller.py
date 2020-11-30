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

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    fitness_class = fitness_class_repository.select(request.form['fitness_class_id'])
    member = member_repository.select_by_membership_no(request.form['membership_no'])
    
    new_booking = Booking(member, fitness_class)
    booking_repository.add(new_booking)
    return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')