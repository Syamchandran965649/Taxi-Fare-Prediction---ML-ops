# from src.ingestion.ingestion import DataIngestion

# if __name__ == "__main__":

#     ingestion = DataIngestion()

#     df = ingestion.initiate_data_ingestion()

#     print(df.head())

# running validation check

# from src.ingestion.ingestion import DataIngestion
# from src.validation.validation import DataValidation


# ingestion = DataIngestion()

# df = ingestion.initiate_data_ingestion()

# validator = DataValidation()

# report = validator.validate_dataset(df)

# print(report)


# from src.ingestion.ingestion import DataIngestion
# from src.validation.validation import DataValidation
# from src.preprocessing.preprocessing_pipeline import DataPreprocessing


# def main():

#     # -----------------------------
#     # Data Ingestion
#     # -----------------------------
#     ingestion = DataIngestion()

#     df = ingestion.initiate_data_ingestion()

#     print("\nData Ingestion Completed")
#     print(f"Dataset Shape : {df.shape}")

#     # -----------------------------
#     # Data Validation
#     # -----------------------------
#     validator = DataValidation()

#     report = validator.validate_dataset(df)

#     if not report["validation_status"]:
#         print("\nData Validation Failed")
#         print(report)
#         return

#     print("\nData Validation Successful")

#     # -----------------------------
#     # Data Preprocessing
#     # -----------------------------
#     preprocessing = DataPreprocessing()

#     processed_df = preprocessing.transform(df)

#     processed_df.to_parquet(
#     "data/processed/processed.parquet",
#     index=False
#     )

#     print("\nData Preprocessing Completed")

#     print(f"Processed Shape : {processed_df.shape}")

#     print("\nFirst Five Records")

#     print(processed_df.head())


# if __name__ == "__main__":

#     main()


# import pandas as pd

# df = pd.read_parquet("data/processed/processed.parquet")

# print(df.columns.tolist())

import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.model_training.train import main

if __name__ == "__main__":
    main()