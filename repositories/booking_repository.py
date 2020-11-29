from db.run_sql import run_sql
from models.fitness_class import FitnessClass
from models.class_type import ClassType
from models.member import Member
from models.booking import Booking

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
    result = run_sql(sql, values)
    id = result[0]['id']
    booking.id = id

#edit
#select all
#select