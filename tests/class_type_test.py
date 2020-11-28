import unittest
from models.class_type import ClassType

class TestClassType(unittest.TestCase):

    def setUp(self):
        self.body_pump = ClassType("Body Pump", "Barbell workout to music. Great for building strength and lean muscle!", "High", "Moderate")

    def test_class_type_has_all_details(self):
        self.assertEqual("Body Pump", self.body_pump.name)
        self.assertEqual("Barbell workout to music. Great for building strength and lean muscle!", self.body_pump.description)
        self.assertEqual("High", self.body_pump.intensity)
        self.assertEqual("Moderate", self.body_pump.difficulty)