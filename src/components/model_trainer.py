import os
import sys
from dataclasses import dataclass

from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            models = {
                "Decision Tree": DecisionTreeClassifier(),
                "XGBClassifier": XGBClassifier(n_estimators=4000, learning_rate=0.05, n_jobs=7 ),
                }

            logging.info('Balance the data using smote')

            X_train, y_train = SMOTE(random_state=42).fit_resample(X_train, y_train)

            logging.info('Smote balance done')


            model_report: dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                                                 models=models)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            logging.info(f"Best found model on both training and testing dataset : {best_model} ")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            accuracy = accuracy_score(y_test, predicted)
            logging.info(f"The score of the best model found is : {accuracy} ")

            return r2_square




        except Exception as e:
            raise CustomException(e, sys)