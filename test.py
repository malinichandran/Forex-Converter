from unittest import TestCase
from app import app

class Flasktests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure all the input from the user is received correctly"""

        with self.client:
            response = self.client.get('/home')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>',html)
            
    def test_convert(self):
        with self.client:
            response = self.client.post('/convert', data = {'convert from':'USD', 'convert to':'INR','amount':10.0})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('msg', html)