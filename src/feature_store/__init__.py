from feast import FeatureStore

class FeatureRetriever:

    def __init__(self):
        self.store = FeatureStore(
            repo_path="feature_store/feature_repo/feature_repo"
        )

    def get_historical_features(self, entity_df):
        return self.store.get_historical_features(
            entity_df=entity_df,
            features=[
                "trip_features:trip_distance",
                "trip_features:pickup_hour",
                "trip_features:pickup_day",
                "trip_features:pickup_month",
                "trip_features:pickup_weekday",
                "trip_features:passenger_count",
            ],
        ).to_df()

    def get_online_features(self, entity_rows):
        return self.store.get_online_features(
            features=[
                "trip_features:trip_distance",
                "trip_features:pickup_hour",
                "trip_features:pickup_day",
                "trip_features:pickup_month",
                "trip_features:pickup_weekday",
                "trip_features:passenger_count",
            ],
            entity_rows=entity_rows,
        ).to_dict()