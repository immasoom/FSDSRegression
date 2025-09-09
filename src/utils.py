### Any common Functionality like reading sql, mongodb etc  #####

import os
import sys
import pickle # creating a pickle file form the model
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):  ###file_path of picke file, obj is the preprocessor
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
