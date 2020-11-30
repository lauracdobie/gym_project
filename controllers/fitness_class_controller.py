from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.class_type import ClassType
import repositories.fitness_class_repository as fitness_class_repository
import repositories.class_type_repository as class_type_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

@fitness_classes_blueprint.route("/fitness-classes")
def upcoming_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/index.html", fitness_classes = fitness_classes)

@fitness_classes_blueprint.route("/fitness-classes/add", methods=['GET'])
def new_class():
    class_types = class_type_repository.select_all()
    return render_template("fitness_classes/add.html", class_types = class_types)

@fitness_classes_blueprint.route("/fitness-classes", methods=['POST'])
def create_fitness_class():
    class_type = class_type_repository.select(request.form['class_type_id'])
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    instructor = request.form['instructor']
    location = request.form['location']
    capacity = request.form['capacity']

    # print("🐰" + class_type.name + "🐰")

    new_class = FitnessClass(class_type, date, time, duration, instructor, capacity, location)
    fitness_class_repository.add(new_class)
    return redirect('/fitness-classes')

@fitness_classes_blueprint.route("/fitness-classes/<id>/participant-list")
def display_participants(id):
    fitness_class = fitness_class_repository.select(id)
    participant_list = fitness_class_repository.get_participants(fitness_class)

    return render_template("fitness_classes/participant_list.html", participant_list = participant_list)