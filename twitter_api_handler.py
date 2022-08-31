from collections import namedtuple
import constants
import requests


Tweet = namedtuple('Tweet', ['id', 'text'])


class TwitterApiHandler:
    """
    Potential values:

    Empty string: only upon initialization
    Some token: when a pagination token is returned after requesting tweets
    -1: if tweets have been requested but no pagination token was returned. This indicates that no more tweets are
        available and no more requests should be made.
    """
    next_page_token = ""

    def get_next_liked_tweets(self) -> [Tweet]:
        if self.next_page_token == "-1":
            return []

        url = 'https://api.twitter.com/2/users/' + str(constants.USER_ID_TO_GET_LIKES_FROM) \
              + '/liked_tweets?max_results=' + constants.TWEETS_PER_REQUEST
        if self.next_page_token != "":
            url += '&pagination_token=' + self.next_page_token
        headers = {'Authorization': 'Bearer ' + constants.BEARER_TOKEN}

        response = requests.get(url, headers=headers).json()

        parsed_response = self._get_tweets_from_json(response)
        self._get_next_page_token(response)

        return parsed_response

    def reset(self):
        self.next_page_token = ""

    def _get_next_page_token(self, tweet_json):
        metadata = tweet_json["meta"]
        next_token = "-1"
        if "next_token" in metadata:
            next_token = metadata["next_token"]
        self.next_page_token = next_token

    @staticmethod
    def _get_tweets_from_json(tweet_json) -> [Tweet]:
        tweets = []
        for tweet in tweet_json["data"]:
            tweets.append(Tweet(tweet["id"], tweet["text"]))
        return tweets
