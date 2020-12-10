import unittest
import os
import requests
from flask import Flask, request, render_template
from pyramid import testing

class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.parameters = {
			'phrase': "I'm going to France for my hollidays"
		}
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
		
	def test_getTop10SimilarTweet(self):
		params = {
			'tweet': self.parameters['phrase']
		}		
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()