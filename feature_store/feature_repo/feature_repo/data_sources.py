from feast import FileSource

trip_source = FileSource(

    path="../../../data/processed/processed.parquet",

    timestamp_field="pickup_datetime"

)