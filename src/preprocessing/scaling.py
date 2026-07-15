import joblib

from sklearn.preprocessing import StandardScaler

class FeatureScalar:
    def __init__(self):
        self.scalar=StandardScaler()
    
    def fit_transform(self,X):
        X_scaled=self.scalar.fit_transform(X)
        joblib.dump(
            self.scalar,"model/artifacts/scalar.pkl"
        )

        return X_scaled
    
    def transform(self,X):
        return self.scalar.transform(X)