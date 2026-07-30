import os
import joblib


class ModelSaver:

    @staticmethod
    def save(
        model,
        path
    ):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        joblib.dump(
            model,
            path
        )