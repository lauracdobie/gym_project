from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.class_type import ClassType
import repositories.fitness_class_repository as fitness_class_repository
import repositories.class_type_repository as class_type_repository
import datetime

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

@fitness_classes_blueprint.route("/fitness-classes/<id>/edit", methods=['GET'])
def edit_fitness_class_details(id):
    class_types = class_type_repository.select_all()
    fitness_class = fitness_class_repository.select(id)
    return render_template("fitness_classes/edit.html", fitness_class = fitness_class, class_types = class_types)

@fitness_classes_blueprint.route("/fitness-classes/<id>", methods=['POST'])
def update_fitness_class_details(id):
    class_type = class_type_repository.select(request.form['class_type_id'])
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    instructor = request.form['instructor']
    location = request.form['location']
    capacity = request.form['capacity']

    updated_class = FitnessClass(class_type, date, time, duration, instructor, capacity, location, id)
    fitness_class_repository.edit(updated_class)
    return redirect('/fitness-classes')

@fitness_classes_blueprint.route("/fitness-classes/<id>/delete", methods=['POST'])
def delete_fitness_class(id):
    fitness_class_repository.delete(id)
    return redirect('/fitness-classes')

@fitness_classes_blueprint.route("/fitness-classes/<id>/description")
def view_class_description(id):
    fitness_class = fitness_class_repository.select(id)
    return render_template("fitness_classes/class_description.html", fitness_class = fitness_class)

@fitness_classes_blueprint.route("/fitness-classes/find_classes-by-class-type")
def find_class_type_form():
    class_types = class_type_repository.select_all()
    return render_template("fitness_classes/find_classes_by_class_type.html", class_types = class_types)

@fitness_classes_blueprint.route("/fitness-classes/found-classes", methods=['POST'])
def display_found_classes():
    class_type = class_type_repository.select(request.form['class_type_id'])
    fitness_classes = fitness_class_repository.find_classes_by_class_type(class_type)

    return render_template("fitness_classes/found_classes.html", fitness_classes = fitness_classes)

@fitness_classes_blueprint.route("/fitness-classes/find-classes-by-duration")
def find_classes_by_duration_form():
    return render_template("fitness_classes/find_classes_by_duration.html")

@fitness_classes_blueprint.route("/fitness-classes/find-classes-by-duration", methods=['POST'])
def display_found_classes_by_duration():
    duration = request.form['duration']
    fitness_classes = fitness_class_repository.find_classes_by_duration(duration)

    # for fitness_class in fitness_classes:
    #     class_type = class_type_repository.select(fitness_class.class_type.id)
    #     date = fitness_class.date
    #     time = fitness_class.time
    #     formatted_date = date.strftime("%d/%m/%Y")
    #     formatted_time = time.strftime("%I:%M") 

    return render_template("fitness_classes/found_classes.html", fitness_classes=fitness_classes)
