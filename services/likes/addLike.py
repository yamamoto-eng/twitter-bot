import setting
import services
import inspect

client = services.clientV2.client
enable = setting.add_like_enable
query = setting.add_like_query
count = setting.add_like_count


def addLike():

    if enable == False:
        return

    print(inspect.currentframe().f_code.co_name)
    execute_num = 1
    tweets = client.search_recent_tweets(query, max_results=100).data
    for tweet in tweets:
        if count < execute_num:
            break
        if tweet.text.startswith("RT") or tweet.text.startswith("@"):
            continue
        client.like(tweet_id=tweet.id)
        print(execute_num, tweet.text)
        execute_num = execute_num + 1
