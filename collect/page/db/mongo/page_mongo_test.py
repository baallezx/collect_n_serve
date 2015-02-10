from pymongo import MongoClient as mc
d = {"hello":"world!!!","does_it":"work"}
import page_mongo as pm
tt = pm.page_mongo("brand_new_data")
tt.insert(d)
