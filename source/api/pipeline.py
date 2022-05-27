"""
Creator: Ivanovitch Silva / José Marcos Leal B. Filho / Lucas Ismael Campos Medeiros
Date: 24 Maio 2022
Define classes used in the pipeline
"""
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Select a Feature
class FeatureSelector(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self, feature_names):
        self.feature_names = feature_names
        
    # Return self nothing to do here
    def fit(self, X, y=None):
        return self
    
    # Method that describes what tis custom transformer need to do
    def transform(self, X, y=None):
        return X[self.feature_names]
    
# Handling categorical features
class CategoricalTransformer(BaseEstimator, TransformerMixin):
    # Class constructor method that takes one boolean as argument
    def __init__(self, new_features=True, colnames=None):
        self.new_features = new_features
        self.colnames = colnames
        
    # Return self nothing else to do here
    def fit(self, X, y=None):
        return self
    
    def get_feature_names_out(self):
        return self.colnames.tolist()
    
    # Transformer method we wrote for this transformer
    def transform(self, X, y=None):
        df = pd.DataFrame(X, columns=self.colnames)
        
        # Remove white space in categorical features
        df = df.apply(lambda row: row.str.strip())
        
        # customize feature?
        # How can I identify what needs to be modified? EDA!!!!!!
        if self.new_features:
            
            # replace ? with unknown
            edit_cols = ['Geography', 'Gender']
            for col in edit_cols:
                df.loc[df[col].str.contains("\?"), col] = 'unknown'
        
        # update column names
        self.colnames = df.columns
        df = pd.DataFrame(X, columns=self.colnames)
        
        return df

# transform numerical features
class NumericalTransformer(BaseEstimator, TransformerMixin):
    # Class constructor method that takes a model parameter as its argument
    # model 0: minmax
    # model 1: standard
    # model 2: without scaler
    def __init__(self, model=0, colnames=None):
        self.model = model
        self.colnames = colnames
        self.scaler = None

    # Fit is used only to learn statistical about Scalers
    def fit(self, X, y=None):
        df = pd.DataFrame(X, columns=self.colnames)
        
        # minmax
        if self.model == 0:
            self.scaler = MinMaxScaler()
            self.scaler.fit(df)
        # standard scaler
        elif self.model == 1:
            self.scaler = StandardScaler()
            self.scaler.fit(df)
        return self

    # return columns names after transformation
    def get_feature_names_out(self):
        return self.colnames

    # Transformer method we wrote for this transformer
    # Use fitted scalers
    def transform(self, X, y=None):
        df = pd.DataFrame(X, columns=self.colnames)
        
        # update columns name
        self.colnames = df.columns.tolist()

        # minmax
        if self.model == 0:
            # transform data
            df = self.scaler.transform(df)
        elif self.model == 1:
            # transform data
            df = self.scaler.transform(df)
        else:
            df = df.values

        return df