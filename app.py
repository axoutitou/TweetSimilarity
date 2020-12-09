from flask import Flask, request, render_template
#import pickle

app = Flask(__name__)


#LOADING example
# with open('vectorizer.pkl', 'rb') as f:
# 	vectorizer = pickle.load(f)

def getTop10SimilarTweet(param_tweet):
    result = {}
    for i in range(10):
        result['tweet'+ str(i)] = "Here is the result for tweet"+ str(i)
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
    app.run(host='0.0.0.0')