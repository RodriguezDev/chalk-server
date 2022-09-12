import constants
import requests


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
    _headers = {'Authorization': 'Bearer ' + constants.TWITTER_BEARER_TOKEN}
    _total_tweets_parsed = 0

    def __init__(self, page_token_to_start_from=''):
        self._next_page_token = page_token_to_start_from
        self._user_id = self._get_user_id_for_username()
        print("User ID for @{}: {}".format(constants.TWITTER_USERNAME_TO_GET_LIKES_FROM, self._user_id))

    def get_next_liked_tweets(self):
        if self._next_page_token is None:
            print("No more liked tweets available to fetch")
            return []

        url = 'https://api.twitter.com/2/users/' + self._user_id + '/liked_tweets?max_results=' \
              + str(constants.TWEETS_PER_REQUEST) + '&tweet.fields=created_at%2Cauthor_id'
        if self._next_page_token != '':
            url += '&pagination_token=' + self._next_page_token

        response = requests.get(url, headers=self._headers).json()
        self._get_next_page_token(response)
        parsed_tweets = self._get_tweets_from_json(response)

        self._total_tweets_parsed += len(parsed_tweets)
        print("Retrieved & parsed {} tweets, {} tweets total. Next page token: {}"
              .format(len(parsed_tweets), self._total_tweets_parsed, self._next_page_token))

        return parsed_tweets

    def reset(self):
        self._total_tweets_parsed = 0
        self._next_page_token = ''

    def _get_user_id_for_username(self) -> str:
        url = 'https://api.twitter.com/2/users/by/username/' + constants.TWITTER_USERNAME_TO_GET_LIKES_FROM
        response = requests.get(url, headers=self._headers).json()
        return response['data']['id']

    def _get_next_page_token(self, tweet_json):
        metadata = tweet_json['meta']
        self._next_page_token = metadata['next_token'] if 'next_token' in metadata else None

    @staticmethod
    def _get_tweets_from_json(tweet_json):
        if tweet_json['meta']['result_count'] == 0:
            return []
        return [{'_id': tweet['id'],
                 'text': tweet['text'],
                 'author_id': tweet['author_id'],
                 'created_at': tweet['created_at']}
                for tweet in tweet_json['data']]
