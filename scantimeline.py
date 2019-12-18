import tweepy
import logging
from   mostFav import save_most_fav
from   mostRT  import save_most_rt

#config logger if one hasn't been initialized yet
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def scan_returnfav_rt(api, mostFav, mostRT):

    #itterate over tweets w/out dealing with pages
    for tweet in tweepy.Cursor(api.user_timeline, 
            screen_name="@every_exception",
            tweet_mode="extended").items(3):

        logger.info(f"Checking tweet ID...{tweet.id}")

        #tweet is a retweet...
        if tweet.retweeted:
            try:
                if tweet.retweeted_status.user.id == api.me().id:
                    logger.info(tweet.user.id)
                    logger.info("\nMATCHED MYSELF, SKIPPING TWEET\n")
                    continue
            except Exception as e:
                logger.error(f"Error on checking tweet: {e}",exc_info=True)
                logger.info("Skipping this tweet\n")
                continue
            mostFav = save_most_fav(tweet, mostFav)
            mostRT  = save_most_rt(tweet, mostRT)
    #return core tweet id
    return mostFav.retweeted_status.id, mostRT.retweeted_status.id