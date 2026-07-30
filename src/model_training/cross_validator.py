from sklearn.model_selection import cross_val_score
import numpy as np

class CrossValidator:

    @staticmethod

    def evaluate(
        model,
        X,
        y,
        cv=5,
        scoring="neg_root_mean_squared_error"
    ):

        scores=cross_val_score(
            estimator=model,
            X=X,
            y=y,
            cv=cv,
            scoring=scoring,
            n_jobs=-1
        )

        rmse_scores=-scores

        return {
            "cv_mean_rmse": np.mean(rmse_scores),
            "cv_std_rmse": np.std(rmse_scores),
            "cv_scores": rmse_scores
        }