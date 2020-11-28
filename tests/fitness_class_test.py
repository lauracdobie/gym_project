import unittest
from models.fitness_class import FitnessClass
from models.class_type import ClassType

class TestFitnessClass(unittest.TestCase):

    def setUp(self):
        self.class_type = self.body_pump = ClassType("Body Pump", "Barbell workout to music. Great for building strength and lean muscle!", "High", "Moderate")
        self.body_pump_express = FitnessClass(self.class_type, "03/12/2020", "14:00", "30 minutes", "Charlotte Anderson", 20, "Studio 1")

    def test_fitness_class_has_all_details(self):
        self.assertEqual("Body Pump", self.body_pump_express.class_type.name)
        self.assertEqual("03/12/2020", self.body_pump_express.date)
        self.assertEqual("14:00", self.body_pump_express.time)
        self.assertEqual("30 minutes", self.body_pump_express.duration)
        self.assertEqual("Charlotte Anderson", self.body_pump_express.instructor)
        self.assertEqual(20, self.body_pump_express.capacity)
        self.assertEqual("Studio 1", self.body_pump_express.location)