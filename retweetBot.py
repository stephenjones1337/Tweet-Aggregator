import tweepy
import logging
import time
from   config import create_api
from   my_filter import my_filter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class RetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me  = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        #avoid RTing replies or myself
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return

        if not tweet.retweeted:
            #retweet unretweeted tweet
            try:
                tweet.retweet()                
                time.sleep(10)
                
            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

    def on_error(self, status_code):
        logger.error(status_code)

def stream(keywords):
    api = create_api()    
    tweets_listener = RetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"], is_async=True)

if __name__ == "__main__":
    stream(["#100daysofcode"])