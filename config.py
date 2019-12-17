# tweepy-bots\bot\config.py
import logging
import tweepy
import os

logger = logging.getLogger()

def create_api():
    #reads environment variables
    consumer_key        = os.getenv("CONSUMER_KEY")
    consumer_secret     = os.getenv("CONSUMER_SECRET")
    access_token        = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    #create auth obj
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #create API obj - tweepy waits and prints a message when rate limit is exceeded
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        #check if creds are valid
        api.verify_credentials()
    except Exception as e:
        #logs error
        logger.error("Error creating API", exc_info=True)
        raise e
    
    logger.info("API created")
    return api