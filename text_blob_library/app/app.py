# from flask import Flask,render_template
# import spacy
# import pickle
# import random

# # train_data = pickle.load(open('/content/train_data.pkl','rb'))

# app=Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# # @app.route('/predict',method=['POST'])
# # def sentimentAnalysis():




# if __name__=="__main__":
#     app.run()

from flask import Flask, render_template, request 
from textblob import TextBlob

app = Flask(__name__)

@app.route('/') # default route
def new():
	result = ""
	return render_template('index.html', result = result) # renders template: index.html with argument result = ""

@app.route('/result', methods = ['POST','GET']) # /result route, allowed request methods; POST, and GET
# def predict():
# 	if request.method == 'POST': 
# 		result = request.form['exp'] # fetches text from <input name = "Name"> from index.html
# 		b = TextBlob(result)
# 		for sentence in b.sentences:
# 			result = sentence.sentiment.polarity
#         # result = polarity value
# 		return render_template('index.html', result = res) # renders template: index.html with argument result = polarity value calculated
# 	else:
# 		return render_template('index.html')	

def predict():
    if request.method == 'POST':
        result=request.form['exp']
        b=TextBlob(result)
        for s in b.sentences:
            result=s.sentiment.polarity
        if result == 0:
            res="Neutral"
        elif result < 0:
            res="Negative"
        else:
            res="Positive"
        return render_template('index.html', result=res)
    else:
        return render_template('index.html')		

if __name__ == '__main__':
	app.debug = True
	app.run()