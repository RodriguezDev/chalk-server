######################
# Mongo DB Constants #
######################

# URL for a Mongo DB server
# Should include the username, password, and other relevant info
MONGO_SRV_URL = 'mongodb+srv://username:password@cluster.xyz.mongodb.net/'
# Name of the database that will be used
# A database will be created with this name if one does not exist already
MONGO_DATABASE_NAME = 'name'
# Collection that will be populated with all the liked tweets
# A collection will be created with this name if one does not exist already
# This collection will be created in the database defined above
MONGO_DATABASE_COLLECTION = 'collection'
