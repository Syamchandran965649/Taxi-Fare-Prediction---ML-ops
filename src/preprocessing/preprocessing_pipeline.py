from src.preprocessing.missing_values import MissingValueHandler
from src.preprocessing.outliers import OutlierHandler
from src.preprocessing.encoder import Encoder
from src.preprocessing.scaling import FeatureScalar
from src.utils.constants import PROCESSED_DATA_PATH
from src.feature_engineering.feature_builder import(FeatureBuilder)
from src.utils.logger import logger

class DataPreprocessing:
    def transform(self,df):

        logger.info("Starting Data Preprocessing")

        df=MissingValueHandler().transform(df)

        df=OutlierHandler().transform(df)

        df=FeatureBuilder().transform(df)

        df=Encoder().transform(df)

        # create processed directory if it doesnot exist already

        PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

        output_file=PROCESSED_DATA_PATH/"processed.csv"
        df.to_csv(output_file,index=False)
        logger.info(f"Processed dataset saved to {output_file}")

        return df