import pandas as pd

class DateTimeFeatures:
    def transform(self,df):
          df["pickup_datetime"]=pd.to_datetime(
               df['pickup_datetime']
          )

          df["pickup_year"]=df["pickup_datetime"].dt.year

          df["pickup_month"]=df["pickup_datetime"].dt.month

          df["pickup_day"]=df["pickup_datetime"].dt.day

          df["pickup_hour"]=df["pickup_datetime"].dt.hour

          df["pickup_weekday"]=(
               df["pickup_datetime"].dt.weekday
          )

          return df