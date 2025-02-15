import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "mode.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
        try:
            logging.info("Initializing model trainer...")

            X_train, Y_train, X_test, Y_test = ( train_array[:,:-1],
                                                train_array[-1],
                                                test_array[:,:-1],
                                                test_array[-1] )

            models = {
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "K-Neighbors" : KNeighborsRegressor(),
                "XGBClassifier" : XGBRegressor(),
                "CatBoosting" : CatBoostRegressor(verbose=False),
                "AdaBoost Classifier" : AdaBoostRegressor()
            }

            model_report:dict=evaluate_models(X_train=X_train, Y_train=Y_train,
                                              X_test=X_test, Y_test=Y_test,
                                              models=models)

            ## to get best model score from dictionary
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.5:
                raise CustomException("No best model found with score", sys)

            logging.info(f"Best model: {best_model_name} with score: {best_model_score}")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            r2_square=r2_score(y_test, predicted)

            return r2_square

        except Exception as e:
            logging.error("Failed to initialize model trainer", error_detail=sys)
            raise Exception("Failed to initialize model trainer") from e