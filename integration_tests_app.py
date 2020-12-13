import unittest
import os
import requests
from flask import Flask, request, render_template
from pyramid import testing
import time

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
		response = requests.post('http://host.docker.internal:5000', data=params)
		self.assertEqual(response.status_code, 200)
		
	def test_1000RequestsPerMinute(self):
		start = time.process_time()
		params = {
			'tweet': self.parameters['phrase']
		}
		for i in range(1000):
			response = requests.post('http://host.docker.internal:5000', data=params)
			self.assertEqual(response.status_code, 200)
				
		request_time = time.process_time() - start
		print(f'Process time is {int(request_time % 60)}')
		self.assertTrue(request_time < now.replace(hour=0, minute=0, second=60, microsecond=0))
		
		
		
	
		

if __name__ == '__main__':
	unittest.main()
