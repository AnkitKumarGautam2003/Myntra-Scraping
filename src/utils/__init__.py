from src.cloud_io import MongoIO
from src.constant import MONGO_DATABASE_NAME
from src.exception import CustomeException
import os,sys

def fetch_product_name_from_cloud():
    try:
        mongo=MongoIO()
        collection_names=mongo.mongo_ins
        return[collection_name.replace("_"," ") for collection_name in collection_names]
    
    except Exception as e:
        raise CustomeException(e,sys)