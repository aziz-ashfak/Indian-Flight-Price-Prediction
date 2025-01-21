import pandas as pd 
import  numpy as np
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import sys
import os
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.logger import logging
from src.exception import CustomException
from src.utilts import save_data

logging.info("Imported modules successfully")

@dataclass
class DataTransformationConfig:
    
    data_preprocessingObJ = os.path.join('artifacts','preprocessor.pkl')
    colum_obj = os.path.join('artifacts','column_data.pkl')
    logging.info("DataTransformationConfig class is created successfully")
    
class DataTranformation:
    
   
            
    def __init__(self):
        
        self.TransformConfig = DataTransformationConfig()
        self.inputs_cols=[ 'airline',  
                          'source_city', 
                          'departure_time',
                          'stops', 
                          'arrival_time',
                          'destination_city',
                          'class', 
                          'duration',
                          'days_left'
                          ]
        self.targets_col='price'
        
    def DataPreprocessingOBJ(self):
        
        try:
            
           
            numerical_features = [ 
                            'duration', 
                             'days_left' 
                                ] 
            categorical_features = [ 
                        'airline', 
                        'source_city', 
                        'departure_time',
                        'stops',
                        'arrival_time',
                        'destination_city',
                        'class'
                        ]
    
            logging.info("seperating numerical and categorical features")
            
            numeric_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',MinMaxScaler())
                ]
            )
            logging.info("Created numeric pipeline")
            
            categorical_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OneHotEncoder(sparse_output=False,handle_unknown='ignore'))
                ]
            )
            logging.info("Created categorical pipeline")
            
            preprocessor = ColumnTransformer(
                transformers = [
                    ('numeric_pipeline',numeric_pipeline,numerical_features),
                    ('cat_pipeline',categorical_pipeline,categorical_features)
                ]
            )
            logging.info("Created preprocessor")
            
            # save all columns name 
            data = {
                'numerical_features':numerical_features,
                'categorical_features':categorical_features,
                "input_cols":self.inputs_cols,
                "target_col":self.targets_col
            }
            
            save_data(
                file_path = self.TransformConfig.colum_obj,
                data = data
            )
            logging.info("save column object!!!")
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def DataPreprocessing(self,train_path,test_path):
        
        try :
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read data successfully")
            
            
            preprocessor = self.DataPreprocessingOBJ()
            logging.info("Got preprocessor object")
            
            # remove the outlier
            train_df = train_df[train_df.price <=100000]
            test_df = test_df[test_df.price <=100000]
            
            # drop Unnamed: 0 and flight that cannnot be used in model
            # Unnamed: 0 is the repiation of index 
            # Flight has 1500++ category this is include flight name which is cannot be a independent variable
            
            train_input = train_df.drop(columns=['Unnamed: 0','flight','price'],axis=1)
            train_target = train_df['price']
            logging.info("Seperated input and target from train data")
            
            test_input = test_df.drop(columns=['Unnamed: 0','flight','price'],axis=1)
            test_target = test_df['price']
            logging.info("Seperated input and target from test data")
            
            train_input = preprocessor.fit_transform(train_input[self.inputs_cols])
            logging.info("Transformed train input data")
            
            test_input = preprocessor.transform(test_input[self.inputs_cols])
            logging.info("Transformed test input data")
            
            # Save the preporcessor
            
            save_data(
                file_path = self.TransformConfig.data_preprocessingObJ,
                data = preprocessor
                )
            
            train_arr = np.c_[
                train_input,np.array(train_target)
            ]
            test_arr = np.c_[
                test_input,np.array(test_target)            
                ]
            return  (
                train_arr,
                test_arr
                )
        except Exception as e:
            raise CustomException(e,sys)