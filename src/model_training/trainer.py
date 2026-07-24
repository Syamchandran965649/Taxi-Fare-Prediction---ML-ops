from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from  src.utils.common import read_yaml

from src.utils.logger import logger

from sklearn.ensemble import RandomForestRegressor

from src.model_training.evaluate import regression_metrics


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

    def train_random_forest(self):

        logger.info("Training Random Forest...\n")
        logger.info('-'*50)

        self.model=RandomForestRegressor(
            random_state=self.config["train"]["random_state"]
        )

        self.model.fit(
            self.X_train,
            self.y_train
        )

        self.y_pred=self.model.predict(
            self.X_test
        )

        self.metrics=regression_metrics(self.y_test,self.y_pred)

        logger.info("Random Forest Training Completed\n")

        logger.info("Evaluation Metrics")

        for metric,value in self.metrics.items():
            logger.info(f"{metric}: {value:.4f}")
            print(f"{metric}: {value:.4f}")
        return self.model,self.metrics
