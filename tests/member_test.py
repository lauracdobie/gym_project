import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.claire = Member("Claire Whittaker", "10 Smith Street", "07783902109", True, 1004)

    def test_member_has_all_details(self):
        self.assertEqual("Claire Whittaker", self.claire.name)
        self.assertEqual("10 Smith Street", self.claire.address)
        self.assertEqual("07783902109", self.claire.phone)
        self.assertEqual(True, self.claire.premium)
        self.assertEqual(1004, self.claire.membership_no)
