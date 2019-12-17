import tweepy
import logging
import json
import time
from   config       import create_api

#config logger if one hasn't been initialized yet
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def save_most_fav(tweet, mostFav):
    logger.info(f"Processing tweet id {tweet.id}\n")
    
    logger.info(f"Currently scanned tweet's favorite count...{tweet.retweeted_status.favorite_count}")
    current_favs  = tweet.retweeted_status.favorite_count
    try:
        mostFav_count = mostFav.retweeted_status.favorite_count
        logger.info(f"Highest favorite count saved...{mostFav_count}\n")
    except:
        mostFav_count = 0
        logger.error("No retweet_status found, assigning mostFav_count to zero")

       

    try:
        if current_favs >= mostFav_count:
            mostFav = tweet
            print(f"Assigned new most favorite tweet...{mostFav.retweeted_status.favorite_count}\n")
            #print(dir(tweet))
            #return tweet
    except Exception as e:
        logger.error("Error on saving mostLiked", exc_info=True)

    return mostFav