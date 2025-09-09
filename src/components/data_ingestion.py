import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # in this we dnt want any functionality and dont need init funciton to
                                  # initialize the variable.we just create class variable
from src.components.data_transformation import DataTransformation

"""
Data Ingestion
   Input: Source path, read Data
   Output: Train and Test split
"""

### Initialize data ingestion configuration
#artifcats is a folder
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

### create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig() # as soon as we create object of this, path of above 3 files will be
                                                    # stored in ingestion_config

    def initiate_data_ingestion(self):
        logging.info("Data ingestion method starts")
        try:
            df=pd.read_csv(os.path.join("notebooks/data","gemstone.csv"))
            logging.info("dataset read as pandas Dataframe")
            ### Please note that EDA has to be done before hand

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set, test_set=train_test_split(df,test_size=.3,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)       
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)    

            logging.info("Ingestion of data is completed")   

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info("Exception occured at Data Ingestion Stage")
            raise CustomException(e,sys)
        
### run data ingestion
"""
if __name__=="__main__":
    obj=DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()
"""

if __name__=="__main__":
    obj=DataIngestion()
    train_data_path , test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)




        

