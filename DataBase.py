import pymongo
import config

log_in = config.log_in_mongodb

VK_DataBase_client = pymongo.MongoClient(f"mongodb+srv://{log_in}@microservice.kbgupzn.mongodb.net/?retryWrites=true&w=majority")
db = VK_DataBase_client.microservice