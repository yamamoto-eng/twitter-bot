import setting
import services

client = services.clientV2.client
user_id = services.clientV2.user_id
enable = setting.delete_like_enable
count = setting.delete_like_count


def deleteLike():

    if enable == False:
        return

    liked_tweets = client.get_liked_tweets(user_id).data
    execute_num = 0
    for liked_tweet in liked_tweets:
        if count <= execute_num:
            break
        client.unlike(liked_tweet.id)
        execute_num = execute_num + 1
