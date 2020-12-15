from flask import Flask, request, render_template
from prometheus_client import start_http_server
from prometheus_client import Counter, Gauge, Summary
import pickle
import time

REQUESTS = Counter('tweetSimilarity_requests_total', 'How many time the application has been accessed')
LAST = Gauge('tweetSimilarity_last_accessed_gauge', 'When was the application last accessed')
LATENCY = Summary('tweetSimilarity_latency', 'Time needed for a request')
EXCEPTIONS = Counter('tweetSimilarity_exceptions_total', 'How many time the applications issued an exception')

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
	model = pickle.load(f)
	
with open('documents.pkl', 'rb') as f:
	documents = pickle.load(f)

def getTop10SimilarTweet(param_tweet):
	new_sentence = param_tweet.split(" ")
	res = model.docvecs.most_similar(positive=[model.infer_vector(new_sentence)],topn=20)	
	result = {}
	i = 0
	for tag, score in res:
		result['tweet'+ str(i)] = ("Sentence : ", documents[tag].words," | Score :", score )
		i = i + 1
		
	return result

@app.route('/', methods=['GET', 'POST'])
def index():
	
	REQUESTS.inc()
	start = time.time()
	LAST.set(start)

	if request.method == 'POST' :
		details = request.form
		form_type = details['send_form']
		if(form_type == 'Submit'):
			result = getTop10SimilarTweet(details['tweet'])
			LATENCY.observe(time.time()-start)
			return render_template('index.html', result=result)
		
		else:
			with EXCEPTIONS.count_exceptions() :
				raise Exception
		
	else :
		LATENCY.observe(time.time()-start)
		return render_template('index.html')

if __name__ == '__main__':
    start_http_server(8010)
    app.run(host='0.0.0.0')