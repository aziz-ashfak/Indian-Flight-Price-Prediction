import os 
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor,BaggingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException
from src.utilts import save_data
from src.utilts import find_best_model,save_data,compress

@dataclass
class ModelTrainerConfig:
    model_path = os.path.join('artifacts','model.pkl.zst')
class ModelTrainer :  
    
    def __init__(self):
        
        self.model_config = ModelTrainerConfig()
        
    def model_trainer(self,train_arr,test_arr):
        
        try:
            X_train,y_train = train_arr[:,:-1],train_arr[:,-1]
            X_test,y_test = test_arr[:,:-1],test_arr[:,-1]
            models = {
                "LinearRegression " : LinearRegression(),
                "RidgeRegression" : Ridge(),
                #"RandomForestReg" : RandomForestRegressor(),This takes a lot of time
                # make a large file after compressing so we avoid it 
                "AdaBoostReg" : AdaBoostRegressor(),
                "GradBoostReg" : GradientBoostingRegressor(),
                "BaggingReg" : BaggingRegressor(),
                "XGBoostReg" : XGBRegressor()
            }
            
            model_result = find_best_model( X_train=X_train,
                                        y_train = y_train,
                                        X_test =X_test,
                                        y_test = y_test,
                                        models = models
                                        )
                   
            # find best accuracy 
            best_result = max(sorted(model_result.values()))
            
            # best model _name 
            
            best_model_name = list(model_result.keys())[
                    list(model_result.values()).index(best_result)
                    ]
            
            best_model = models[best_model_name]
            
            # Model will be a large file so we should compress it 
            compress(
                file_path = self.model_config.model_path ,
                data = best_model
                )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square
            
        except Exception as e:
            raise CustomException(e,sys)
    
    
