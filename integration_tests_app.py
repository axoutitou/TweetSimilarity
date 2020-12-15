import unittest
import os
import requests
from flask import Flask, request, render_template
from pyramid import testing
from time import perf_counter

class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.parameters = {
			'phrase': "I'm going to France for my hollidays"
			'send_form':"Submit"
		}
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
		
	def test_getTop10SimilarTweet(self):
		params = {
			'tweet': self.parameters['phrase']
			'send_form' : self.parameters['send_form']
		}		
		response = requests.post('http://host.docker.internal:5000', data=params)
		self.assertEqual(response.status_code, 200)
		
	def test_1000RequestsPerMinute(self):
		start = perf_counter()
		params = {
			'tweet': self.parameters['phrase']
			'send_form' : self.parameters['send_form']
		}
		for i in range(1000):
			response = requests.post('http://host.docker.internal:5000', data=params)
			self.assertEqual(response.status_code, 200)
				
		stop = perf_counter()
		elapsed_time = stop - start
		print(f'Process time is {elapsed_time}')
		self.assertTrue(elapsed_time < 60.0)
		
if __name__ == '__main__':
	unittest.main()
