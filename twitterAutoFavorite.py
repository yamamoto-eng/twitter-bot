import tweepy
import os
from dotenv import load_dotenv
import editSetting

load_dotenv()

client = tweepy.Client(
    os.getenv("BEARER_TOKEN"),
    os.getenv("API_KEY"),
    os.getenv("API_KEY_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET"),
)


def addLike():
    if editSetting.add_like_enable == False:
        return
    else:
        query = editSetting.add_like_query
        count = editSetting.add_like_count
        tweets = client.search_recent_tweets(query, max_results=count)[0]
        for tweet in tweets:
          client.like(tweet_id=tweet.id, user_auth=True)

addLike()
