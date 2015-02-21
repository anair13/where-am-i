from pymongo import MongoClient
from bson.binary import Binary
import pickle

client = MongoClient()
db = client.localize
features_collection = db.features # maps filenames to features and metadataID
metadata_collection = db.metadata # stores any metadata about images (locations, captions, etc)

def write_items(features, metadata):
    """Write features with common metadata to Mongo"""
    metadataID = metadata_collection.insert(metadata)
    for feature in features:
        f = Binary(pickle.dumps(feature, protocol=2), subtype=128 )
        feature_item = {"features": f, "metadataID": metadataID}
        features_collection.insert(feature_item)

def write_item(feature_array, metadata):
    write_items([feature_array], metadata)

def get_all_images():
    for x in features_collection.find():
        yield pickle.loads(x['features']), x['metadataID']

def get_meta(id):
    return metadata_collection.find_one({"_id": id})

if __name__ == "__main__":
    print metadata_collection.find_one()
    print features_collection.count()