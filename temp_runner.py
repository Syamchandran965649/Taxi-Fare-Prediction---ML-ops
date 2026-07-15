# from src.ingestion.ingestion import DataIngestion

# if __name__ == "__main__":

#     ingestion = DataIngestion()

#     df = ingestion.initiate_data_ingestion()

#     print(df.head())

# running validation check

from src.ingestion.ingestion import DataIngestion
from src.validation.validation import DataValidation


ingestion = DataIngestion()

df = ingestion.initiate_data_ingestion()

validator = DataValidation()

report = validator.validate_dataset(df)

print(report)