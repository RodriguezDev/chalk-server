from collections import namedtuple
import constants
import requests

Tweet = namedtuple('Tweet', ['id', 'text'])


class TwitterApiHandler:
    """
    Page token potential values:

    Empty string: only upon initialization
    Some token: when a pagination token is returned after requesting tweets
    None: if tweets have been requested but no pagination token was returned. This indicates that no more tweets are
        available and no more requests should be made.
    """
    _next_page_token = ''
    _user_id = None
    _headers = {'Authorization': 'Bearer ' + constants.BEARER_TOKEN}

    def __init__(self):
        self._user_id = self._get_user_id_for_username()
        print("User ID for @{}: {}".format(constants.USERNAME_TO_GET_LIKES_FROM, self._user_id))

    def get_next_liked_tweets(self) -> [Tweet]:
        if self._next_page_token is None:
            print("No more liked tweets available to fetch")
            return []

        url = 'https://api.twitter.com/2/users/' + self._user_id + '/liked_tweets?max_results=' \
              + str(constants.TWEETS_PER_REQUEST)
        if self._next_page_token != "":
            url += '&pagination_token=' + self._next_page_token

        response = requests.get(url, headers=self._headers).json()
        self._get_next_page_token(response)
        parsed_response = self._get_tweets_from_json(response)

        print("Retrieved & parsed {} tweets. Next page token: {}".format(len(parsed_response), self._next_page_token))
        return parsed_response

    def reset(self):
        self._next_page_token = ''

    def _get_user_id_for_username(self) -> str:
        url = 'https://api.twitter.com/2/users/by/username/' + constants.USERNAME_TO_GET_LIKES_FROM
        response = requests.get(url, headers=self._headers).json()
        return response['data']['id']

    def _get_next_page_token(self, tweet_json):
        metadata = tweet_json['meta']
        self._next_page_token = metadata['next_token'] if 'next_token' in metadata else None

    @staticmethod
    def _get_tweets_from_json(tweet_json) -> [Tweet]:
        return [Tweet(tweet['id'], tweet['text']) for tweet in tweet_json['data']]
