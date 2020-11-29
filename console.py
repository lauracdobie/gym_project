import pdb
from models.member import Member
from models.class_type import ClassType
from models.fitness_class import FitnessClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.class_type_repository as class_type_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
class_type_repository.delete_all()
fitness_class_repository.delete_all()

claire = Member("Claire Whittaker", "10 Smith Street", "07783902109", "clairem89@gmail.com", True, 1004)
member_repository.add(claire)

angela = Member("Angela O'Shaughnessy", "12 Smith Street", "07785976809", "angelaO79@gmail.com", False, 895)
member_repository.add(angela)

body_pump = ClassType("Body Pump", "Barbell workout to music. Great for building strength and lean muscle!", "High", "Moderate")
class_type_repository.add(body_pump)

body_balance = ClassType("Body Balance", "A mix of yoga, tai chi and pilates. Great for mobility", "Low", "Low")
class_type_repository.add(body_balance)

body_pump_express = FitnessClass(body_pump, "03/12/2020", "14:00", "30 minutes", "Charlotte Anderson", 20, "Studio 1")
fitness_class_repository.add(body_pump_express)

body_balance_am = FitnessClass(body_balance, "04/12/2020", "10:00", "55 minutes", "Madeleine Johnson", 8, "Studio 2")
fitness_class_repository.add(body_balance_am)

body_balance_am = FitnessClass(body_balance, "05/12/2020", "18:00", "45 minutes", "Anna Murray", 15, "Studio 1")
fitness_class_repository.edit(body_balance_am)

booking_1 = Booking(angela, body_pump_express)
booking_repository.add(booking_1)

booking_2 = Booking(claire, body_balance_am)

pdb.set_trace()