from flask import Flask,request,app,render_template,url_for,jsonify
import numpy as np
import pandas as pd 
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
#nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import pickle
app=Flask(__name__)

scaler=pickle.load(open('vectorizer.pkl','rb'))
predictor=pickle.load(open('model.pkl','rb'))


def transformation(text):
    text=str(text).lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form['input_data']
        data=transformation(data)
        v_data=scaler.transform([data])
        result=predictor.predict(v_data[0])
        if result==1:
            data="SPAM"
        else:
            data="NOT SPAM"
        return render_template('home.html', data=data)
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True) 
