import unittest
import app
import six

class TestAPP(unittest.TestCase):

	# Tests whether the function returns a not empty result
	def test_getTop10SimilarTweet_returnsResult(self):
		self.assertTrue(app.getTop10SimilarTweet("I'm going to France for my hollidays"))

	# Tests whether the function returns twenty tweets into the result
	def test_getTop10SimilarTweet_returnsTwentyTweets(self):
		self.assertEqual(len(app.getTop10SimilarTweet("I'm going to France for my hollidays")), 20)
		
	# Tests whether the result is a dictionnary of tweets
	def test_getTop10SimilarTweet_returnsStringDictionnary(self):
		self.assertTrue(type(six.next(six.itervalues(app.getTop10SimilarTweet("I'm going to France for my hollidays")))), str)
		
if __name__ == '__main__':
	unittest.main()
		
	
if __name__ == '__main__':
	unittest.main()