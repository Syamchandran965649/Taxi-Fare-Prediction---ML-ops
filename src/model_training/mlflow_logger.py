import mlflow
import mlflow.sklearn

class MLFlowLogger:

    @staticmethod
    def log_model(
        model,
        metrics,
        params,
        cv_results,
        model_name
    ):
        mlflow.set_experiment("Taxi-Fare Prediction")
        with mlflow.start_run():

            for key,value in params.items():
                mlflow.log_param(key,value)

            for key,value in metrics.items():
                mlflow.log_metric(key,value)

            mlflow.log_metric(
            "cv_rmse_mean",
            cv_results["cv_mean_rmse"]
            )

            mlflow.log_metric(
                "cv_rmse_std",
                cv_results["cv_std_rmse"]
            )

            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model"
            )


