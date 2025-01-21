import pandas as pd 
import numpy as np
import sys
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.logger import logging
from src.exception import CustomException
from src.component.data_tranformation import DataTransformationConfig
from src.component.data_tranformation import DataTranformation
from src.component.model_trainner import ModelTrainerConfig
from src.component.model_trainner import ModelTrainer
@dataclass
class DataIngestionConfig:
    
    raw_data_path:str = os.path.join('artifacts','raw_data.csv')
    train_data_path:str = os.path.join('artifacts','train_data.csv')
    test_data_path:str = os.path.join('artifacts','test_data.csv')
    logging.info("DataIngestionConfig class is created successfully")
    
class DataIngestion:
    
    def __init__(self):
        
        self.IngestConfig = DataIngestionConfig()
    
    def  data_spilter(self):
        
        try:
            df = pd.read_csv('Dataset/Clean_Dataset.csv')
            logging.info("Data read successfully")
            
            df.to_csv(self.IngestConfig.raw_data_path,index=False,header=True)
            logging.info("Data saved successfully")
            
            train_df,test_df = train_test_split(df,test_size=0.2,random_state=42)
            logging.info("Data splitted successfully")
            
            train_df.to_csv(self.IngestConfig.train_data_path,index=False,header=True)
            logging.info("Train data saved successfully")
            
            test_df.to_csv(self.IngestConfig.test_data_path,index=False,header=True)
            logging.info("Test data saved successfully")
            
            return (self.IngestConfig.train_data_path,
                    self.IngestConfig.train_data_path
                    )
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__ == '__main__':
    ingestion = DataIngestion()
    train_df_path,test_df_path = ingestion.data_spilter()
    
    preprocesse = DataTranformation()
    train_arr,test_arr = preprocesse.DataPreprocessing(train_df_path,test_df_path )
    
    trainner = ModelTrainer()
    
    print("The best model accuracy is  : ",trainner.model_trainer(train_arr,test_arr))
    
    
    