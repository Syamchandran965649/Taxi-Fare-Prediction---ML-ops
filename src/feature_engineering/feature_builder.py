from src.feature_engineering.haversine import HaversineDistance
from src.feature_engineering.datetime_features import DateTimeFeatures

class FeatureBuilder:

    def transform(self,df):

        df=DateTimeFeatures().transform(df)
        df["trip_distance"]=HaversineDistance.calculate(
            df["pickup_latitude"],

            df["pickup_longitude"],

            df["dropoff_latitude"],

            df["dropoff_longitude"]
        )

        df.drop(
            columns=["pickup_datetime"],
            inplace=True
        )
        return df