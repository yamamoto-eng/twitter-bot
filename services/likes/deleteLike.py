import setting
import services
import inspect

client = services.clientV2.client
user_id = services.clientV2.user_id
enable = setting.delete_like_enable
count = setting.delete_like_count


def deleteLike():
    if enable == False:
        return

    print(inspect.currentframe().f_code.co_name)
    liked_tweets = client.get_liked_tweets(user_id).data
    execute_num = 1
    for liked_tweet in liked_tweets:
        if count < execute_num:
            break
        client.unlike(liked_tweet.id)
        print(liked_tweet.text)
        execute_num = execute_num + 1
