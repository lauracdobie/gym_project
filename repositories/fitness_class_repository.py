from db.run_sql import run_sql
from models.fitness_class import FitnessClass
import models.class_type as ClassType
from models.member import Member
import repositories.class_type_repository as class_type_repository
import repositories.member_repository as member_repository
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
    fitness_class.id = id

#edit
def edit(fitness_class):
    sql = "UPDATE fitness_classes SET (class_type_id, date, time, duration, instructor, capacity, location) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [fitness_class.class_type.id, fitness_class.date, fitness_class.time, fitness_class.duration, fitness_class.instructor, fitness_class.capacity, fitness_class.location, fitness_class.id]
    result = run_sql(sql, values)

# select all
def select_all():
    all_fitness_classes = []
    sql = "SELECT * FROM fitness_classes ORDER BY date ASC, time ASC"
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

def get_participants(fitness_class):
    participant_list = []
    sql = """SELECT members.*
                FROM members
                INNER JOIN bookings ON members.id = bookings.member_id
                INNER JOIN fitness_classes ON fitness_classes.id = bookings.fitness_class_id
                WHERE fitness_classes.id = %s"""

    values = [fitness_class.id]
    sql_results = run_sql(sql, values)
    
    for row in sql_results:

        participant = Member(row['name'], row['address'], row['phone'], row['email'], row['premium'], row['membership_no'], row['id'])
        participant_list.append(participant)
    
    return participant_list

def find_classes_by_class_type(class_type):
    found_classes = []
    sql = "SELECT * from fitness_classes WHERE class_type_id = %s"
    value = [class_type.id]
    results = run_sql(sql, value)

    for result in results:
        found_class = FitnessClass(class_type, result['date'], result['time'], result['duration'], result['instructor'], result['capacity'], result['location'], result['id'])
        found_classes.append(found_class)
    
    return found_classes

def find_classes_by_duration(duration):
    found_classes = []
    sql = "SELECT * from fitness_classes WHERE duration <= %s"
    value = [duration]
    results = run_sql(sql, value)

    for result in results:
        class_type = class_type_repository.select(result['class_type_id'])
        found_class = FitnessClass(class_type, result['date'], result['time'], result['duration'], result['instructor'], result['capacity'], result['location'], result['id'])
        found_classes.append(found_class)
    
    return found_classes
    
  