import pandas as pd

from src.ingestion.ingestion import DataIngestion

# check whether the dataset returns a non-empty dataframe

def test_ingestion():

    ingestion = DataIngestion()

    df = ingestion.initiate_data_ingestion()

    assert isinstance(df, pd.DataFrame)

    assert len(df) > 0

    assert df.shape[1] > 0