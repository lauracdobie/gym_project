import unittest
from models.member import Member

def test_member_has_all_details(self):
    claire = Member("Claire Whittaker", "10 Smith Street", "07783902109", True, 1004)
    self.assertEqual("Claire Whittaker", claire.name)
    self.assertEqual("10 Smith Street", claire.address)
    self.assertEqual("07783902109", claire.phone)
    self.assertEqual(True, claire.premium)
    self.assertEqual(1004, claire.membership_no)
