from collections import namedtuple
import constants
import requests


Tweet = namedtuple('Tweet', ['id', 'text'])


class TwitterApiHandler:

    def get_tweets_for_user(self) -> [Tweet]:
        url = 'https://api.twitter.com/2/users/' + str(constants.USER_ID_TO_GET_LIKES_FROM) + '/liked_tweets?max_results=100'
        headers = {'Authorization': 'Bearer ' + constants.BEARER_TOKEN}
        response = requests.get(url, headers=headers)

        parsed_response = self._get_tweets_from_json(response.json())
        return parsed_response

    @staticmethod
    def _get_tweets_from_json(tweet_json) -> [Tweet]:
        tweets = []
        for tweet in tweet_json["data"]:
            tweets.append(Tweet(tweet["id"], tweet["text"]))

        return tweets
