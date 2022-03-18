from unittest import TestCase
from xml.dom import UserDataHandler
from app import app
from flask import session
from forex_python.converter import CurrencyRates

class FlaskTests(TestCase):

    def setUp(self):
        """To do before each test"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_convert(self):

        self.client.get('/')
        fromCurr = 'USD'
        toCurr = 'USD'
        amount = '1'
        c = CurrencyRates()
        self.assertEqual(c.convert(fromCurr.upper(), toCurr.upper(), float(amount)), 1.0)
    
