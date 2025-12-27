import pandas as pd
from sklearn.base import BaseEstimator,TransformerMixin


# class for data cleaning
class DataCleaner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X["V_TAT"] = X["V_TAT"].fillna(0)
        X["C_TAT"] = X["C_TAT"].fillna(0)
        X["Driver_Ratings"] = X["Driver_Ratings"].fillna(0)
        X["Customer_Rating"] = X["Customer_Rating"].fillna(0)
        X["Payment_Method"] = X["Payment_Method"].fillna("Not Applicable")

        return X

# class for feature engineering
class FlagVariableGenerator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X["V_TAT_IND"] = (X["V_TAT"] > 0).astype(int)
        X["C_TAT_IND"] = (X["C_TAT"] > 0).astype(int)
        X["Payment_Method_Ind"]=(X["Payment_Method"]!="Not Applicable").astype(int)
        X["Driver_Ratings_Ind"] = (X["Driver_Ratings"] > 0).astype(int)
        X["Customer_Rating_Ind"] = (X["Customer_Rating"] > 0).astype(int)

        return X

# class for datetime extracting
class DateTimeExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, datetime_col="Date"):
        self.datetime_col = datetime_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X[self.datetime_col] = pd.to_datetime(X[self.datetime_col])
        dt = X[self.datetime_col]

        X["Month"] = dt.dt.month
        X["weekday"] = dt.dt.weekday
        X["date"] = dt.dt.day
        X["booking_hour"] = dt.dt.hour
        X["meridiem"] = dt.dt.hour.apply(lambda h: "AM" if h < 12 else "PM")
        X["day_type"] = dt.dt.weekday.apply(lambda d: "weekend" if d in [5, 6] else "weekday")

        X.drop(columns=[self.datetime_col], inplace=True)
        return X
