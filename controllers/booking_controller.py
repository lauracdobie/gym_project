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