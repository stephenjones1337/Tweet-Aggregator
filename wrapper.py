import tweepy
import json
from   scantimeline import scan_returnfav_rt
from   config       import create_api



def init_fav():
    mostFav = tweepy.Status
    return mostFav

def init_retweet():
    mostRT = tweepy.Status
    mostRT.retweet_count = 0
    return mostRT

def get_tweets():
    api     = create_api()
    mostFav = init_fav()
    mostRT  = init_retweet()

    #get tweet ids
    tweet_id_collection = scan_returnfav_rt(api, mostFav, mostRT)
    #convert to json and return
    return json.dumps(tweet_id_collection)
    #end while