import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

# Load the data
file_path = "diabetes.csv"
diabetes = pd.read_csv(file_path)

def check_null(diabetes):
    return diabetes.isnull().sum()
# print(check_null(diabetes))

df_copy = diabetes.copy(deep=True)
df_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = df_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)


df_copy['Glucose'].fillna(df_copy['Glucose'].mean(), inplace=True)
df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean(), inplace=True)
df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median(), inplace=True)
df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace=True)
df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace=True)


# Split the data
x = df_copy.drop(columns = "Outcome")
y = df_copy['Outcome']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42, stratify=y)

svc_linear = SVC(kernel='linear')
svc_linear.fit(X_train,y_train)

def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age):
    # Create a DataFrame with the user input
    user_input = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [diabetes_pedigree],
        'Age': [age]
    })
    
    prediction = svc_linear.predict(user_input)

    return prediction

result = predict_diabetes(6, 148, 72, 35, 125, 33.6, 0.267, 50)

if result == 0:
    print('Non diabetic')
else:
    print('Diabetic')

print(result)

pickle.dump(svc_linear, open('diabetes_model.pkl', 'wb'))
