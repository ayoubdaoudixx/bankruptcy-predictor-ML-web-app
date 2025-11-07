import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, atr1: float,
    atr2: float,
    atr3: float,
    atr4: float,
    atr5: float,
    atr6: float,
    atr7: float,
    atr8: float,
    atr9: float,
    atr10: float,
    atr11: float,
    atr12: float,
    atr13: float,
    atr14: float,
    atr15: float,
    atr16: float,
    atr17: float,
    atr18: float,):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3
        self.atr4 = atr4
        self.atr5 = atr5
        self.atr6 = atr6
        self.atr7 = atr7
        self.atr8 = atr8
        self.atr9 = atr9
        self.atr10 = atr10
        self.atr11 = atr11
        self.atr12 = atr12
        self.atr13 = atr13
        self.atr14 = atr14
        self.atr15 = atr15
        self.atr16 = atr16
        self.atr17 = atr17
        self.atr18 = atr18

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict ={
            "atr1": [self.atr1],
            "atr2": [self.atr2],
            "atr3": [self.atr3],
            "atr4": [self.atr4],
            "atr5": [self.atr5],
            "atr6": [self.atr6],
            "atr7": [self.atr7],
            "atr8": [self.atr8],
            "atr9": [self.atr9],
            "atr10": [self.atr10],
            "atr11": [self.atr11],
            "atr12": [self.atr12],
            "atr13": [self.atr13],
            "atr14": [self.atr14],
            "atr15": [self.atr15],
            "atr16": [self.atr16],
            "atr17": [self.atr17],
            "atr18": [self.atr18],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)