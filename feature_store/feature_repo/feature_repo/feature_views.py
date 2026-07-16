from feast import FeatureView
from feast import Field
from feast.types import Float32
from feast.types import Int64
from datetime import timedelta
from entities import trip
from data_sources import trip_source

trip_features=FeatureView(
    name="trip_features",
    entities=[trip],
    ttl=timedelta(days=365),
    schema=[
        Field(name="trip_distance",dtype=Float32),
        Field(name="pickup_hour",dtype=Int64),
        Field(name="pickup_day",dtype=Int64),
        Field(name="pickup_month",dtype=Int64),
        Field(name="pickup_weekday",dtype=Int64),
        Field(name="passenger_count",dtype=Int64),
    ],
    source=trip_source,
    online=True
)
