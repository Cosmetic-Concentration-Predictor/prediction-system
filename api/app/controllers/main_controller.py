from flask import Flask, jsonify, request
from flask_cors import CORS
from app.services.prediction_service import PredictionService

app = Flask(__name__)
CORS(app)

prediction_service = PredictionService()


@app.route("/api/predict", methods=["POST"])
def predict_concentration():
    data = request.get_json()
    acronyms = [x.upper() for x in data.get("acronyms")]
    codes = data.get("codes")

    predictions_response = prediction_service.predict_concentrations(acronyms, codes)
    predictions = []

    for i in range(len(predictions_response.concentrations)):
        predictions.append(
            {
                "acronym": predictions_response.acronyms[i],
                "code": predictions_response.codes[i],
                "concentration": predictions_response.concentrations[i],
            }
        )

    return jsonify(predictions)
