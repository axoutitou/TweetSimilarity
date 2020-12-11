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
		
	def test_1000RequestsPerMinute(self):
		start = time.clock()
		params = {
			'tweet': self.parameters['phrase']
		}
		for i in (0,1000)
			response = requests.post('http://localhost:5000', data=params)
			self.assertEqual(response.status_code, 200)
				
		request_time = time.clock() - start
		minuteToCompare = now.replace(hour=0, minute=1, second=0, microsecond=0)
		print(request_time)
		self.assertTrue(request_time < minuteToCompare)

if __name__ == '__main__':
	unittest.main()
