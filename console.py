import pdb
from models.member import Member
# from models.class_type import ClassType
# from models.fitness_class import FitnessClass
# from models.booking import Booking

import repositories.member_repository as member_repository
# import repositories.class_type_repository as class_type_repository
# import repositories.fitness_class_repository as fitness_class_repository
# import repositories.booking_repository as booking_repository

member_repository.delete_all()

claire = Member("Claire Whittaker", "10 Smith Street", "07783902109", "clairem89@gmail.com", True, 1004)
member_repository.add(claire)

angela = Member("Angela O'Shaughnessy", "12 Smith Street", "07785976809", "angelaO79@gmail.com", False, 895)
member_repository.add(angela)

claire = Member("Clare Whittaker", "14 Smith Street", "07783902109", "clairem89@gmail.com", True, 1004)
member_repository.edit(claire)

pdb.set_trace()