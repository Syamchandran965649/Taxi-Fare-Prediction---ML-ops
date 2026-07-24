from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from src.utils.common import read_yaml


class ModelCollection:

    def __init__(self, 
                    config_path:str="configs/model.yaml",
                    data_path:str='data/processed/processed.parquet'):
            self.config=read_yaml(config_path)

    # @staticmethod
    def get_models(self):

        return {
            "RandomForest":RandomForestRegressor(
                n_estimators=self.config["train"]["n_estimators"],
                random_state=self.config["train"]["random_state"],
                n_jobs=self.config["train"]["n_jobs"]
            ),
            "XGBoost":XGBRegressor(
                n_estimators=self.config["train"]["n_estimators"],
                random_state=self.config["train"]["random_state"],
                max_depth=self.config["train"]["max_depth"],
                learning_rate=self.config["train"]["learning_rate"],
                objective=self.config["train"]["objective"],
            ),
            "LightGBM":LGBMRegressor(
                n_estimators=self.config["train"]["n_estimators"],
                random_state=self.config["train"]["random_state"],
                learning_rate=self.config["train"]["learning_rate"],
            )

        }