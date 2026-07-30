from pathlib import Path

import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from  src.utils.common import read_yaml

from src.utils.logger import logger

from sklearn.ensemble import RandomForestRegressor


from src.model_training.evaluate import regression_metrics
from src.model_training.mlflow_logger import MLFlowLogger
from src.model_training.model_collection import ModelCollection
from src.model_training.tuner import ModelTuner
from src.model_training.cross_validator import CrossValidator


class ModelTrainer:

    def __init__(self, 
                config_path:str="configs/model.yaml",
                data_path:str='data/processed/processed.parquet'):
        self.config=read_yaml(config_path)
        self.data_path=Path(data_path)

        self.df=None

        self.xtrain=None
        self.xtest=None  

        self.ytrain=None
        self.ytest=None

        self.model=None
        self.y_pred=None
        self.metrics=None

    def load_data(self):
       logger.info("Loading processed dataset...")
       print("Loading processed dataset...") 
       self.df=pd.read_parquet(self.data_path)
       print(f"Dataset shape:{self.df.shape}")
       return self.df 
    
    def split_data(self):

        logger.info('Performing train-test split')
        logger.info("="*30)
        target=self.config["train"]['target_column']

        X=self.df.drop([target,"key","pickup_datetime"],axis=1)

        y=self.df[target]

        (self.X_train,self.X_test,self.y_train,self.y_test)=train_test_split(
            X,
            y,
            test_size=self.config["train"]["test_size"],
            random_state=self.config["train"]["random_state"]
            )
        print()
        logger.info("train-test Split Completed")
        print("train-test Split Completed")

        print(f"X_train={self.X_train}")
        print(f"X_test={self.X_test}")
        print(f"y_train={self.y_train}")
        print(f"y_test={self.y_test}")

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        )

    def train_model(self,model_name,model):

        logger.info(f"Training {model_name}...\n")
        logger.info('-'*50)

        model.fit(
            self.X_train,
            self.y_train
        )

        self.y_pred=model.predict(
            self.X_test
        )

        self.metrics=regression_metrics(self.y_test,self.y_pred)

        print(self.metrics)

        logger.info(f"{model_name} Training Completed\n")

        cv_results = CrossValidator.evaluate(
        model=model,
        X=self.X_train,
        y=self.y_train
        )

        logger.info("Cross Validation Results")
        logger.info(cv_results)

        # logger.info("Evaluation Metrics")

        # for metric,value in self.metrics.items():
        #     logger.info(f"{metric}: {value:.4f}")
        #     print(f"{metric}: {value:.4f}")

        os.makedirs(
            "artifacts/models",
            exist_ok=True
        )

        model_path=f"artifacts/models/{model_name.lower()}.pkl"

        joblib.dump(
            model,
            model_path
        )

        MLFlowLogger.log_model(
            model=model,
            metrics=self.metrics,
            params={
                "model":model_name
            },
            cv_results=cv_results,
            model_name=model_name
        )
        logger.info("Model Saved Successfully")
        print("\nModel Saved Successfully")
        print(model_path)

        return self.metrics

    def train_all_models(self):

        models = ModelCollection().get_models()

        results = {}

        tuner = ModelTuner(
            self.X_train,
            self.y_train,
        )

        for model_name in models.keys():

            logger.info(f"Tuning {model_name}")

            best_params=tuner.optimize(
                model_name=model_name,
                n_trials=20
            )

            logger.info(best_params)

            model=ModelCollection.build_model(
                model_name,
                best_params
            )

            metrics=self.train_model(
                model_name=model_name,
                model=model
            )

            results[model_name] = metrics
        logger.info("Training Completed")

        return results
