from db.run_sql import run_sql
from models.fitness_class import FitnessClass
import models.class_type as ClassType
import repositories.class_type_repository as class_type_repository
import pdb

#delete all
def delete_all():
    sql = "DELETE  FROM fitness_classes"
    run_sql(sql)


#delete selected
def delete(id):
    sql = "DELETE  FROM fitness_classes WHERE id = %s"
    value = [id]
    run_sql(sql, value)

#add
def add(fitness_class):
    sql = "INSERT INTO fitness_classes (class_type_id, date, time, duration, instructor, capacity, location) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [fitness_class.class_type.id, fitness_class.date, fitness_class.time, fitness_class.duration, fitness_class.instructor, fitness_class.capacity, fitness_class.location]
    result = run_sql(sql, values)
    id = result[0]['id']
    fitness_class.class_type.id = id

#edit
def edit(fitness_class):
    sql = "UPDATE fitness_classes SET (class_type_id, date, time, duration, instructor, capacity, location) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [fitness_class.class_type.id, fitness_class.date, fitness_class.time, fitness_class.duration, fitness_class.instructor, fitness_class.capacity, fitness_class.location, fitness_class.id]
    result = run_sql(sql, values)

# select all
def select_all():
    all_fitness_classes = []
    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)
    # pdb.set_trace()
    for result in results:
        class_type = class_type_repository.select(result['class_type_id'])
        fitness_class = FitnessClass(class_type, result['date'], result['time'], result['duration'], result['instructor'], result['capacity'], result['location'], result['id'])
        all_fitness_classes.append(fitness_class)
    
    return all_fitness_classes

#select
def select(id):
    fitness_class = None
    sql = "SELECT * from fitness_classes WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    class_type = class_type_repository.select(result['class_type_id'])
    fitness_class = FitnessClass(class_type, result['date'], result['time'], result['duration'], result['instructor'], result['capacity'], result['location'], result['id'])
    return fitness_class

  