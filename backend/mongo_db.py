import pymongo
import constants


def get_random_like_from_db():
    client = pymongo.MongoClient(constants.MONGO_SRV_URL)
    db = client[constants.MONGO_DATABASE_NAME]
    liked_tweets_collection = db[constants.MONGO_DATABASE_COLLECTION]
    cursor = liked_tweets_collection.aggregate([{'$sample': {'size': 1}}])

    random_like = [tweet for tweet in cursor]
    return {} if not random_like else random_like[0]
