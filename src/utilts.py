import os
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException
import zstandard as zstd

def save_data(file_path,data):
    
    try:
        with open(file_path,'wb') as file:
            pickle.dump(data,file)
            logging.info(f"Data saved successfully at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)
    
def load_data(file_path):
    try:
        with open(file_path,'rb') as file:
            return pickle.load(file)

    except Exception as e:
        raise CustomException(e,sys)
    

# find the best model 

def find_best_model(X_train,y_train,X_test,y_test,models):
    
    try:
        report = {}
        train_scores = []
        test_scores = []
        train_losses = []
        test_losses = []
        for i in range(len(models)):
            
            model = list(models.values())[i]
            model.fit(X_train,y_train)
            logging.info("Fit the model")
            
            train_score = r2_score(y_train,model.predict(X_train))
            test_score = r2_score(y_test,model.predict(X_test))
            logging.info("Calcutate train test score!!! ")
            
            train_loss = mean_squared_error(y_train,model.predict(X_train))
            test_loss = mean_squared_error(y_test,model.predict(X_test))
            logging.info("Calculate train and test loss!!! ")
            
            train_scores.append(train_score)
            test_scores.append(test_score)
            train_losses.append(train_loss)
            test_losses.append(test_loss)
            logging.info("Append all model observation!!!")
            
            report[list(models.keys())[i]] = test_score
        
        details = {
            "Model": list(models.keys()),
            "Train_score":train_scores,
            "Test_score":test_scores,
            "Train_loss":train_losses,
            "Test_loss":test_losses
        }
        df = pd.DataFrame(details)
        df.to_csv('ResultAnalysis/Result.csv',index=False,header=True)
        logging.info("Details of our research!!!")
        return report
    except Exception as e:
        raise CustomException(e,sys)
    
# compress the large size model 

def compress(file_path,data):
    compressed_model = zstd.ZstdCompressor(level=22).compress(pickle.dumps(data))
    with open(file_path, "wb") as f:
        f.write(compressed_model)

# decompress

def decompress(file_path):
    with open(file_path, "rb") as f:
        return pickle.loads(zstd.ZstdDecompressor().decompress(f.read()))