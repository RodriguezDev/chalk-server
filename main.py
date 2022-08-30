# It's chalk stalk time.

import constants
from twitter_api_handler import TwitterApiHandler


def main():
    handler = TwitterApiHandler()
    print(handler.get_tweets_for_user())


if __name__ == '__main__':
    main()
