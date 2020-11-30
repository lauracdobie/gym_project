from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.class_type import ClassType
import repositories.fitness_class_repository as fitness_class_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

@fitness_classes_blueprint.route("/fitness-classes")
def upcoming_classes():
    fitness_classes = fitness_class_repository.select_all()
    # for class in fitness_classes:
    #     class_type = fitness_class.class_type.name
    return render_template("fitness_classes/index.html", fitness_classes = fitness_classes)