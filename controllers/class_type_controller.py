from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.class_type import ClassType
import repositories.class_type_repository as class_type_repository

class_types_blueprint = Blueprint("class_types", __name__)

@class_types_blueprint.route("/class-types")
def class_type_list():
    class_types = class_type_repository.select_all()
    return render_template("class_types/index.html", class_types=class_types)

@class_types_blueprint.route("/class-types/add", methods=['GET'])
def new_class_type():
    return render_template("class_types/add.html")

@class_types_blueprint.route("/class-types", methods=['POST'])
def create_class_type():
    name = request.form['name']
    description = request.form['description']
    intensity = request.form['intensity']
    difficulty = request.form['difficulty']

    new_class_type = ClassType(name, description, intensity, difficulty)
    class_type_repository.add(new_class_type)
    return redirect('/class-types')

@class_types_blueprint.route("/class-types/<id>/edit", methods=['GET'])
def edit_class_type_details(id):
    class_type = class_type_repository.select(id)
    return render_template("class_types/edit.html", class_type = class_type)

@class_types_blueprint.route("/class-types/<id>", methods=['POST'])
def update_class_type_details(id):
    name = request.form['name']
    description = request.form['description']
    intensity = request.form['intensity']
    difficulty = request.form['difficulty']

    updated_class_type = ClassType(name, description, intensity, difficulty, id)
    class_type_repository.edit(updated_class_type)
    return redirect('/class-types')

@class_types_blueprint.route("/class-types/<id>/delete", methods=['POST'])
def delete_class_type(id):
    class_type_repository.delete(id)
    return redirect('/class-types')