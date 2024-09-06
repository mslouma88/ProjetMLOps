from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("Logistic Regression_best_model.pkl", "rb"))


def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        clo = int(request.form["credit_lines_outstanding"])
        lao = float(request.form["loan_amt_outstanding"])
        tbo = float(request.form["total_debt_outstanding"])
        income = float(request.form["income"])
        ye = int(request.form["years_employed"])
        fs = int(request.form["fico_score"])

        prediction = model.predict([[clo, lao, tbo, income, ye, fs]])

        if prediction[0] == 1:
            return render_template(
                "index.html",
                prediction_text="éligible ! Veuillez prendre rendez-vous avec le client.",
            )

        else:
            return render_template(
                "index.html", prediction_text="Rejeté ! Veuillez avertir le client."
            )

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
