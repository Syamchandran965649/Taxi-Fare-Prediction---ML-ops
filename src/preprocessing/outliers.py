import pandas as pd 
from src.utils.logger import logger

class OutlierHandler:
    def transform(self,df:pd.DataFrame):

        logger.info("Removing Outliers")

        numeric_cols=df.select_dtypes(
            include=['number']
        ).columns

        for col in numeric_cols:
            if col=="passenger_count":
                continue
            Q1=df[col].quantile(0.25)
            Q3=df[col].quantile(0.75)

            IQR=Q3-Q1

            lower=Q1-1.5*IQR
            upper=Q3+1.5*IQR

            df=df[
                (df[col]>=lower)
                &
                (df[col]<=upper)
                ]
        logger.info('Outliers removed')
        return df