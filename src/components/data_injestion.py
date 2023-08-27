import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path= str=os.path.join('artifatcs','train.csv')
    test_data_path= str=os.path.join('artifatcs','test.csv')
    raw_data_path= str=os.path.join('artifatcs','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initate_data_ingestion(self):
        logging.info('Enterted the data ingestion')
        try:
            df=pd.read_csv('data\stud.csv')
            logging.info('Dataset is readed and save in df')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)        
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)        

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Train Test Intiated') 
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=0)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Train Test Split Sucessful')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.initate_data_ingestion()            