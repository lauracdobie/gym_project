import unittest
from models.fitness_class import FitnessClass
from models.class_type import ClassType
from models.member import Member
from models.booking import Booking

class TestBookingClass(unittest.TestCase):
    def setUp(self):
        self.class_type = self.body_pump = ClassType("Body Pump", "Barbell workout to music. Great for building strength and lean muscle!", "High", "Moderate")
        self.body_pump_express = FitnessClass(self.class_type, "03/12/2020", "14:00", "30 minutes", "Charlotte Anderson", 20, "Studio 1")
        self.claire = Member("Claire Whittaker", "10 Smith Street", "07783902109", "clairem89@gmail.com", True, 1004)
        self.booking = Booking(self.claire, self.body_pump_express)

    def test_booking_has_all_details(self):
        self.assertEqual("Claire Whittaker", self.booking.member.name)
        self.assertEqual("Body Pump", self.booking.fitness_class.class_type.name)
        self.assertEqual("14:00", self.booking.fitness_class.time)

