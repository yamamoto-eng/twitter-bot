import setting
import services
import inspect
import datetime

client = services.clientV2.client
enable = setting.delete_retweet_enable
count = setting.delete_retweet_count


def deleteRetweet():
    if enable == False:
        return

    now = datetime.datetime.now()
    my_id = client.get_me().data.id
    execute_num = 1
    tweet_list = client.get_users_tweets(my_id).data
    print(now.strftime("%H時%M分"), inspect.currentframe().f_code.co_name)

    for tweet in tweet_list:
        if count < execute_num:
            break
        print(execute_num)
        print(tweet)
        execute_num = execute_num + 1
