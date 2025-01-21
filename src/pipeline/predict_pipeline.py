
import pickle 
import numpy as np
import pandas as pd
import zstandard as zstd 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.utilts import decompress,load_data

def make_prediction(data):
    model = decompress('artifacts/model.pkl.zst')
    processor  = load_data('artifacts/preprocessor.pkl')
    col_data = load_data('artifacts/column_data.pkl')
    
    df = pd.DataFrame([data])
    X = processor.transform(df[col_data['input_cols']])
    pred = model.predict(X)
    return pred[0]


