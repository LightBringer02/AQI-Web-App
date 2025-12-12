from flask import Flask, render_template, request
import pickle
import numpy as np

def get_aqi_status(aqi):
    if aqi <= 50:
        return "Good", "bg-green-500"
    elif aqi <= 100:
        return "Satisfactory", "bg-lime-500"
    elif aqi <= 200:
        return "Moderate", "bg-yellow-400"
    elif aqi <= 300:
        return "Poor", "bg-orange-500"
    elif aqi <= 400:
        return "Very Poor", "bg-red-600"
    else:
        return "Severe", "bg-purple-700"


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        # Collect input values
        pm2 = float(request.form.get('PM2', 0) or 0)
        pm10 = float(request.form.get('PM10', 0) or 0)
        no = float(request.form.get('NO', 0) or 0)
        no2 = float(request.form.get('NO2', 0) or 0)
        nox = float(request.form.get('NOx', 0) or 0)
        co = float(request.form.get('CO', 0) or 0)
        so2 = float(request.form.get('SO2', 0) or 0)
        o3 = float(request.form.get('O3', 0) or 0)
        ben = float(request.form.get('Benzene', 0) or 0)
        tol = float(request.form.get('Toluene', 0) or 0)
        nh3 = float(request.form.get('NH3', 0) or 0)

        model_choice = request.form['model']

        if model_choice == 'random':
            model = pickle.load(open('model_random.pkl', 'rb'))
            data = np.array([[pm2, pm10, no, no2, nox, nh3, co, so2, o3, ben, tol]])

        elif model_choice == 'xgb':
            model = pickle.load(open('model_xgboost.pkl', 'rb'))
            data = np.array([[pm2, pm10, no, no2, nox, nh3, co, so2, o3, ben, tol]])

        elif model_choice == 'svm':
            model = pickle.load(open('model_svm.pkl', 'rb'))
            data = np.array([[pm2, no2, nh3, co, so2, ben, tol]])

        elif model_choice == 'ensemble':
            model = pickle.load(open('model_ensemble.pkl', 'rb'))
            data = np.array([[pm2, no2, nh3, co, so2, ben, tol]])

        else:
            return "Invalid model selected!"

        my_prediction = model.predict(data)
        pred_value = round(float(my_prediction[0]), 2)

        status, color = get_aqi_status(pred_value)

        return render_template(
            "index.html",
            pred=pred_value,
            status=status,
            color=color,
            pm2=pm2, pm10=pm10, no=no, no2=no2, nox=nox,
            nh3=nh3, co=co, so2=so2, o3=o3, ben=ben, tol=tol
        )

if __name__ == '__main__':
    app.run(debug=True)
