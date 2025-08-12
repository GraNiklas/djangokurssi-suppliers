import unittest
from django.test import TestCase

from django_1.laskin import plus, plus_complicated

class LaskinTest(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen
        self.assertEqual(plus(7,2),9)
        self.assertEqual(plus(7.1,2.7),9.8)
    def test_pluscomplicated(self):
        # testaa että numerot lasketaan yhteen
        self.assertEqual(plus_complicated(7,2),9)
        self.assertEqual(plus_complicated(2,7),7)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus('7',2),9)
        
    #TDD - Test Driven Developement