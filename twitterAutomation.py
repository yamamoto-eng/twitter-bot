import tweepy
import os
from dotenv import load_dotenv
import operation

load_dotenv()

client = tweepy.Client(
    os.getenv("BEARER_TOKEN"),
    os.getenv("API_KEY"),
    os.getenv("API_KEY_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET"),
)


def addLike():
    enable = operation.add_like_enable
    query = operation.add_like_query
    count = operation.add_like_count

    if enable == False:
        return

    execute_num = 0
    tweets = client.search_recent_tweets(query, max_results=100)[0]
    for tweet in tweets:
        if count <= execute_num:
            break
        if tweet.text.startswith("RT") or tweet.text.startswith("@"):
            continue
        client.like(tweet_id=tweet.id, user_auth=True)
        execute_num = execute_num + 1


addLike()
