# Chalk

A way to see forgotten liked tweets.

## Running the tweet populator

To populate the DB with the liked tweets of a given user:

1. Navigate to `tweetpopulator`
2. Supply appropriate values to `constants.py`
3. Run the script using `python3 main.py`

The script will grab all the tweets a user has liked and place them in a DB that we can query below

## Running the backend

To run the backend:

1. Navigate to the `backend` directory and set up a Flask virtual environment following [these instructions](https://flask.palletsprojects.com/en/2.2.x/installation/#virtual-environments)
2. Supply appropriate values to `constants.py`
3. Run the server using `flask --app app run`

You should now be able to query the DB at http://127.0.0.1:5000/
