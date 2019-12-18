import tweepy
import logging
import json
import time
from   config       import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def save_most_rt(tweet, mostRT):
    try:
        #get RT count of current tweet
        current_RTs  = tweet.retweet_count

        #get highest RT count from saved tweet
        mostRT_count = mostRT.retweet_count         
    except:
        logger.error("Error on getting RT count", exc_info=True)
    try:
        if current_RTs >= mostRT_count:
            mostRT = tweet
            logger.info(f"Assigned new most RT tweet...{mostRT.retweet_count}\n")

            return mostRT
    except Exception as e:
        logger.error("Error on saving mostRT", exc_info=True)

    return mostRT