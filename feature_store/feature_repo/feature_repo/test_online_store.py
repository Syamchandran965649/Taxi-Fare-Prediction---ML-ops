from feast import FeatureStore

store = FeatureStore(repo_path=".")

features = store.get_online_features(
    features=[
        "trip_features:trip_distance",
        "trip_features:pickup_hour",
        "trip_features:pickup_day",
        "trip_features:pickup_month",
        "trip_features:pickup_weekday",
        "trip_features:passenger_count",
    ],
    entity_rows=[
        {"key": "2015-05-07 19:52:06.0000003"}
    ],
).to_dict()

print(features)