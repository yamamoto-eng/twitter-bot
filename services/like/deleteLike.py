import setting
import services
import inspect
import datetime

client = services.clientV2.client
enable = setting.delete_like_enable
count = setting.delete_like_count


def deleteLike():

    if enable == False:
        return

    now = datetime.datetime.now()
    my_id = client.get_me().data.id
    execute_num = 1
    liked_tweets = client.get_liked_tweets(my_id).data
    print("\n--------------------------------------------------")
    print(now.strftime("%H時%M分"), inspect.currentframe().f_code.co_name)
    print("--------------------------------------------------\n")

    for liked_tweet in liked_tweets:
        if count < execute_num:
            break
        try:
            client.unlike(liked_tweet.id)
            print("🚀", execute_num, "\n", liked_tweet.text)
            execute_num = execute_num + 1
        except:
            print("\n--------------------------------------------------")
            print("error")
            print("--------------------------------------------------\n")
