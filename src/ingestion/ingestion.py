import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import dotenv
from src.utils.logger import logger
from src.utils.common import read_yaml
from src.utils.constants import CONFIG_PATH,ARTIFACT_DIR
from src.utils.exception import CustomException

class DataIngestion:

    def __init__(self):
        self.config=read_yaml(CONFIG_PATH)
        self.raw_data_path=Path(
            self.config["data"]["raw_data_path"]
        )
        self.artifact_path=ARTIFACT_DIR/"raw.csv"

    def initiate_data_ingestion(self):
        """
        Function that verifies the path of the data

        Returns
        -------

        pandas.DataFrame
        """
        logger.info("="*60)
        logger.info("Starting Data Ingestion")

        try:
            if not self.raw_data_path.exists():
                raise FileNotFoundError(
                    f"Dataset doesnot found:{self.raw_data_path}"
                )
            logger.info(f"Reading dataset:{self.raw_data_path}")
            df=pd.read_csv(self.raw_data_path)
            logger.info(f"Dataset Loaded Successfully")
            logger.info(f"Rows : {df.shape[0]}")
            logger.info(f"Columns : {df.shape[1]}")

            self.artifact_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.copy(
                self.raw_data_path,
                self.artifact_path
            )

            logger.info(
                f"Raw dataset copied to {self.artifact_path}"
                )
            
            logger.info("Data Ingestion Completed")
            logger.info("="*60)

            return df
        except Exception as e:
            logger.exception("Error occured during Data Ingestion")
            raise CustomException(e)
