import pandas as pd

class DateTimeFeatures:
    def transform(self,df):
          df["pickup_datetime"]=pd.to_datetime(
               df['pickup_datetime']
          )

          df["pickup_year"]=df["pickip_datetime"].dt.year

          df["pickup_month"]=df["pickip_datetime"].dt.month

          df["pickup_day"]=df["pickip_datetime"].dt.day

          df["pickup_hour"]=df["pickip_datetime"].dt.hour

          df["pickup_weekday"]=(
               df["pickup_datetime"].dt.weekday
          )

          return df