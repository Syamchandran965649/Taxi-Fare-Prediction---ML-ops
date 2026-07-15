from src.ingestion.ingestion import DataIngestion
from src.validation.validation import DataValidation


def test_validation():

    ingestion = DataIngestion()

    df = ingestion.initiate_data_ingestion()

    validator = DataValidation()

    report = validator.validate_dataset(df)

    assert "validation_status" in report

    assert report["validation_status"] is True