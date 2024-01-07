import numpy as np
from flask import Flask,request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('diabetesModel.pkl','rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
   
    glucose = float(request.form['glucose'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    age = float(request.form['age'])
    input_features = np.array([glucose,insulin,bmi,age])
    input_reshaped = input_features.reshape(1, -1)
    input_features_scaled = scaler.fit_transform(input_reshaped)
    prediction = model.predict(input_features_scaled)
    if(prediction == 0):
        return (render_template('index.html', prediction_text = f"Prediction Non Diabetic: {prediction[0]}") )
    else:
        return (render_template('index.html', prediction_text =  f"Prediction Diabetic: {prediction[0]}" ))

if __name__ == "__main__":
    app.run(port=5000, debug=True)

