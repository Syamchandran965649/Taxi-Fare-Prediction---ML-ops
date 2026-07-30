class ModelComparison:

    @staticmethod
    def get_best_model(cv_results:dict):

        best_model=None
        best_score=float("inf")

        for model_name,metrics in cv_results.items():

            if metrics["cv_mean_rmse"]< best_score:
                best_score=metrics["cv_mean_rmse"]
                best_model=model_name

        return best_model,best_score