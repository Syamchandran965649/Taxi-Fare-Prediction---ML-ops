from src.utils.logger import logger
import pandas as pd

class MissingValueHandler:
    def transform(self,df:pd.DataFrame):
        logger.info("Handling Missing Values")
        numeric_cols=df.select_dtypes(
            include=['number']
        ).columns

        categorical_cols=df.select_dtypes(
            exclude=['number']
        ).columns

        for column in numeric_cols:
            df[column].fillna(
                df[column].median(),
                inplace=True
            )
        for column in categorical_cols:
            df[column].fillna(
                df[column].mode()[0],
                inplace=True
            )
        logger.infor("Missing Values Handled")
        return df