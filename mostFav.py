import tweepy
import logging
import json
import time
from   config       import create_api

#config logger if one hasn't been initialized yet
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def save_most_fav(tweet, mostFav):
    #get favorite count of current tweet
    current_favs  = tweet.retweeted_status.favorite_count

    try:
        #get highest favorite count
        mostFav_count = mostFav.retweeted_status.favorite_count        
    except:
        #assign 0 on first runthrough 
        mostFav_count = 0
    try:
        if current_favs >= mostFav_count:
            mostFav = tweet
            logger.info(f"Assigned new most favorite tweet...{mostFav.retweeted_status.favorite_count}\n")
            
            return mostFav
    except Exception as e:
        logger.error("Error on saving new tweet", exc_info=True)
        
    return mostFav