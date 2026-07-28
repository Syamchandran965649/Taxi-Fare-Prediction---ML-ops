import optuna

from sklearn.model_selection import cross_val_score

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor

class ModelTuner:

    def __init__(self, X_train, y_train):

        self.X_train= X_train
        self.y_train=y_train

    def optimize(self,model_name,n_trials=20):


        def objective(trial):

            if model_name == 'RandomForest':

                model=RandomForestRegressor(

                n_estimators=trial.suggest_int(
                    "n_estimators",
                    100,
                    500,
                    step=50
                ),

                max_depth=trial.suggest_int(
                    "max_depth",
                    5,
                    30
                ),
                min_samples_split=trial.suggest_int(
                "min_samples_split",
                2,
                10
            ),

            min_samples_leaf=trial.suggest_int(
                "min_samples_leaf",
                1,
                5
            ),

            random_state=42,

            n_jobs=-1

        )

        
            elif model_name=='LightGBM':

                model=LGBMRegressor(
                    n_estimators=trial.suggest_int(
                    "n_estimators",
                    100,
                    500,
                    step=50
                ),

                max_depth=trial.suggest_int(
                    "max_depth",
                    3,
                    15
                ),

                learning_rate=trial.suggest_float(
                    "learning_rate",
                    0.01,
                    0.3,
                    log=True
                ),

                random_state=42
                )

            elif model_name=="XGBoost":

                model=XGBRegressor(
                    n_estimators=trial.suggest_int(
                "n_estimators",
                100,
                500,
                step=50
            ),

            max_depth=trial.suggest_int(
                "max_depth",
                3,
                12
            ),

            learning_rate=trial.suggest_float(
                "learning_rate",
                0.01,
                0.3,
                log=True
            ),

            subsample=trial.suggest_float(
                "subsample",
                0.6,
                1.0
            ),

            colsample_bytree=trial.suggest_float(
                "colsample_bytree",
                0.6,
                1.0
            ),

            random_state=42
                )
            else:
                raise ValueError(f"Unknown model: {model_name}")

            score=cross_val_score(
                model,

                self.X_train,

                self.y_train,

                cv=5,

                scoring="neg_root_mean_squared_error",

                n_jobs=-1
            ).mean()

            return score

        study=optuna.create_study(direction='maximize')
        study.optimize(objective,n_trials=n_trials)

        return study.best_params
