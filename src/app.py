## Flask file
import flask
import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

# Initialize
app = Flask(__name__, static_url_path = '', static_folder = 'static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ##
    Y = []
    for i in request.form:
        print(i, request.form[i])
        Y.append(request.form[i])

    Y = pd.DataFrame(Y)
    Y_t = tf_idf.transform([Y.iloc[0,0]]).toarray()
    tf_idf_df = pd.DataFrame(Y_t, columns = tf_idf.get_feature_names())
    Y = Y.drop([0], axis = 0)
    Y = scaler.transform(Y.T)
    scaled_df = pd.DataFrame(Y.T, columns = [0])
    Y = pd.concat((scaled_df, tf_idf_df.T), axis = 0)
    
    severity = int(model.predict(Y.T)[0])

    print(severity)

    if severity <= 0: 
        severity = 'Low severity'
        color = 'var(--blue)'
    elif severity >= 1 and severity <= 4: 
        severity = 'Medium severity'
        color = 'var(--yellow)'
    else: 
        severity = 'High severity'
        color = 'var(--pink)'

    return render_template('index.html', severity = severity, color = color)


if __name__ == '__main__':

    MODEL_PATH = '../models'

    # Load pickles
    with open(f'{MODEL_PATH}/tf_idf.pickle', 'rb') as f:
        tf_idf = pickle.load(f)
    with open(f'{MODEL_PATH}/scaler.pickle', 'rb') as f:
        scaler = pickle.load(f)
    with open(f'{MODEL_PATH}/model.pickle', 'rb') as f:
        model = pickle.load(f)

    app.run()