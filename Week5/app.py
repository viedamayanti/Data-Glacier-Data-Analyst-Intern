import numpy as np
from flask import Flask,request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('diabetes_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    pregnancies = float(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    blood_pressure = float(request.form['blood_pressure'])
    skin_thickness = float(request.form['skin_thickness'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetesPedigree = float(request.form['diabetesPedigree'])
    age = float(request.form['age'])
    input_features = np.array([pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetesPedigree,age])
    input_reshaped = input_features.reshape(1, -1)
    prediction = model.predict(input_reshaped)

    print("Input Features:",input_features)
    print("Input Reshaped:", input_reshaped)
    print("Prediction:", prediction)


    if(prediction == 0):
        return (render_template('index.html', prediction_text = f" Non Diabetic") )
    else:
        return (render_template('index.html', prediction_text =  f" Diabetic Diagnosed"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)

