from pathlib import Path

import pandas as pd

import json

from src.validation.schema import load_schema
from src.utils.logger import logger
from src.utils.exception import CustomException

class DataValidation:
    def __init__(self):
        self.schema=load_schema()

    def validate_dataset(self,dataframe:pd.DataFrame):
        """
        Validate dataframe using schema.yaml
        """
        try:
            logger.info("Starting Data Validation")
            '''
            Datastructure for showing output of validation
            '''
            validation_report={
                "missing_columns":[],
                "datatype_errors":{},
                "validation_status":True
            }

            # -------------------------
            # Check Missing Columns
            # -------------------------

            expected_columns=list(self.schema.columns.keys())
            actual_columns = list(dataframe.columns)

            missing_columns = [
                col 
                for col in expected_columns if col not in actual_columns
            ]

            if missing_columns:

                validation_report["missing_columns"]=missing_columns
                validation_report['validation_status']=False

            # -------------------------
            # Validate Data Types
            # -------------------------

            for column,expected_datatype in self.schema.columns.items():

                if column in dataframe.columns:

                    actual_datatype=str(dataframe[column].dtype)

                    if actual_datatype!=expected_datatype:

                        validation_report["datatype_errors"][column]={
                            "expected":expected_datatype,
                            "found":actual_datatype
                        }

                        validation_report["validation_status"]=False
            Path('artifacts').mkdir(exist_ok=True)

            with open("artifacts/validation_report.json","w") as file:
                json.dump(validation_report,file,indent=4)
            
            if validation_report['validation_status']:
                logger.info("Dataset validation successful")
            else:
                logger.info("Dataset Validation Failed")
            
            return validation_report
        except Exception as e:
            logger.exception("Validation Failed")
            raise CustomException(e)
