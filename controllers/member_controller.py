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

@members_blueprint.route("/members/add", methods=['GET'])
def new_member():
    return render_template("members/add.html")

@members_blueprint.route("/members", methods=['POST'])
def create_member():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    premium = request.form['premium']
    membership_no = request.form['membership_no']

    new_member = Member(name, address, phone, email, premium, membership_no)
    member_repository.add(new_member)
    return redirect('/members')