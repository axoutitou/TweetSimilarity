from flask import Flask, request, render_template
from prometheus_client import start_http_server
import pickle

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
    if request.method == 'POST' :
        details = request.form
        result = getTop10SimilarTweet(details['tweet'])
        return render_template('index.html', result=result)
        
    else :
        return render_template('index.html')

if __name__ == '__main__':
    start_http_server(8010)
    app.run(host='0.0.0.0')