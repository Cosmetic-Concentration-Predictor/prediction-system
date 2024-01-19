from app.models.prediction_model import Prediction
import pandas as pd
import joblib


class PredictionService:
    def __init__(self):
        self.ml_model = joblib.load("ml_models/ml_model.joblib")
        self.ml_encoder = joblib.load("ml_models/ml_encoder.joblib")

    def predict_concentrations(self, acronyms, codes):
        data = self.preprocess_data_to_predict(acronyms, codes)
        concentrations = self.ml_model.predict(data)
        prediction = Prediction(
            acronyms=acronyms, codes=codes, concentrations=concentrations
        )
        return prediction

    def preprocess_data_to_predict(self, acronyms, codes):
        data = pd.DataFrame({"acronym": acronyms, "code": codes})

        acronym_2d = data["acronym"].values.reshape(-1, 1)

        encoded_acronym = self.ml_encoder.transform(acronym_2d)
        encoded_acronym_df = pd.DataFrame(
            encoded_acronym,
            columns=self.ml_encoder.get_feature_names_out(["acronym"]),
        )

        data = pd.concat([data, encoded_acronym_df], axis=1)

        data.drop("acronym", axis=1, inplace=True)
        return data
