# Constants used throughout the script

#########################
# Twitter API Constants #
#########################

# Get this by signing up for a Twitter dev account https://developer.twitter.com/en/portal/petition/essential/basic-info
TWITTER_BEARER_TOKEN = 'token'
# The username of the whose liked tweets will be fetched & stored. Must be public
TWITTER_USERNAME_TO_GET_LIKES_FROM = 'user'
# Maximum tweets that should be processed at a time
# Can be a value between 10 & 100
# Note that this value will be the amount of tweets fetched & also populated in the DB per request.
TWEETS_PER_REQUEST = 10

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
