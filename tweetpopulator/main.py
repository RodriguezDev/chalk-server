from database_handler import DatabaseHandler
import time
from twitter_api_handler import TwitterApiHandler


def main():
    tweet_handler = TwitterApiHandler()
    database_handler = DatabaseHandler()

    while True:
        tweets = tweet_handler.get_next_liked_tweets()
        if not tweets:
            break
        database_handler.insert_tweets(tweets)

        time.sleep(5)


if __name__ == '__main__':
    main()
