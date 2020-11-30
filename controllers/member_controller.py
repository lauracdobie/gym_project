from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.class_type import ClassType
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def member_list():
    all_members = member_repository.select_all()
    return render_template("members/index.html", all_members = all_members)

@members_blueprint.route("/add-member")
def add_member_form():
    return render_template("members/add.html")