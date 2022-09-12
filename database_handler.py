import pymongo
import constants


class DatabaseHandler:
    _client = pymongo.MongoClient(constants.MONGO_SRV_URL)
    _db = None
    _liked_tweets_collection = None

    def __init__(self):
        print("Database {} exists: {}".format(constants.MONGO_DATABASE_NAME,
                                              constants.MONGO_DATABASE_NAME in self._client.list_database_names()))
        self._db = self._client[constants.MONGO_DATABASE_NAME]
        self._liked_tweets_collection = self._db[constants.MONGO_DATABASE_COLLECTION]

    def insert_tweets(self, tweets):
        response = self._liked_tweets_collection.insert_many(tweets)
        print("Added {} tweets to [{}: {}]"
              .format(len(response.inserted_ids), constants.MONGO_DATABASE_NAME, constants.MONGO_DATABASE_COLLECTION))

    def get_random_like(self):
        cursor = self._liked_tweets_collection.aggregate([{'$sample': {'size': 1}}])
        return [tweet for tweet in cursor][0]
