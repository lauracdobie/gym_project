from db.run_sql import run_sql
from models.fitness_class import FitnessClass
from models.class_type import ClassType
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.class_type_repository as class_type_repository
import repositories.fitness_class_repository as fitness_class_repository
import pdb

#delete all
def delete_all():
    sql = "DELETE  FROM bookings"
    run_sql(sql)

#delete selected
def delete(id):
    sql = "DELETE  FROM bookings WHERE id = %s"
    value = [id]
    run_sql(sql, value)

#add
def add(booking):
    sql = "INSERT INTO bookings (member_id, fitness_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.fitness_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking.id
 

#edit
def edit(booking):
    sql = "UPDATE bookings SET (member_id, fitness_class_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.fitness_class.id, booking.id]
    # pdb.set_trace()
    run_sql(sql, values)

#select all
def select_all():
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    all_bookings = []

    for result in results:
        member = member_repository.select(result['member_id'])
        fitness_class = fitness_class_repository.select(result['fitness_class_id'])
        booking = Booking(member, fitness_class, result['id'])
        all_bookings.append(booking)
    
    return all_bookings

#select
def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    member = member_repository.select(result['member_id'])
    fitness_class = fitness_class_repository.select(result['fitness_class_id'])
    booking = Booking(member, fitness_class, result['id'])
    return booking