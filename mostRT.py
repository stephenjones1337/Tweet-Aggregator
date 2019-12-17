import tweepy
import logging
import json
import time
from   config       import create_api

#config logger if one hasn't been initialized yet
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def save_most_rt(tweet, mostRT):
    try:
        logger.info(f"Processing tweet id {tweet.id}\n")

        current_RTs  = tweet.retweet_count
        logger.info(f"Currently scanned tweet's RT count...{current_RTs}")    

        mostRT_count = mostRT.retweet_count
        logger.info(f"Highest RT count saved...{mostRT_count}\n")  
    except:
        logger.error("Error on getting RT count", exc_info=True)
    
    try:
        if current_RTs >= mostRT_count:
            mostRT = tweet
            logger.info(f"Assigned new most RT tweet...{mostRT.retweet_count}\n")
    except Exception as e:
        logger.error("Error on saving mostRT", exc_info=True)

    return mostRT