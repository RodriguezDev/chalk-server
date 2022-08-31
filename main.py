from twitter_api_handler import TwitterApiHandler


def main():
    handler = TwitterApiHandler()

    while True:
        tweets = handler.get_next_liked_tweets()
        if not tweets:
            break


if __name__ == '__main__':
    main()
