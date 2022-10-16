import setting
import services

client = services.clientV2.client
enable = setting.add_like_enable
query = setting.add_like_query
count = setting.add_like_count


def addLike():

    if enable == False:
        return

    execute_num = 0
    tweets = client.search_recent_tweets(query, max_results=100).data
    for tweet in tweets:
        if count <= execute_num:
            break
        if tweet.text.startswith("RT") or tweet.text.startswith("@"):
            continue
        client.like(tweet_id=tweet.id)
        execute_num = execute_num + 1
