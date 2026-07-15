from src.preprocessing.missing_values import MissingValueHandler
from src.preprocessing.outliers import OutlierHandler
from src.preprocessing.encoder import Encoder
from src.preprocessing.scaling import FeatureScalar

from src.feature_engineering.feature_builder import(FeatureBuilder)

class DataPreprocessing:
    def transform(self,df):

        df=MissingValueHandler.transform(df)

        df=OutlierHandler().transform(df)

        df=FeatureBuilder().transform(df)

        df=Encoder().transform(df)

        return df