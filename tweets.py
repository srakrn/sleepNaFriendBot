import tweepy
from datetime import datetime, time
from time import sleep 
import credentials
from texts import get_text

bot_target = 'ryolen_tlkang'
debug = False 

auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_secret)
auth.set_access_token(credentials.token_key, credentials.token_secret)
api = tweepy.API(auth)

f = open('last_tweet_id.txt', 'r')
replied_tweet_id = int(f.read())
f.close()

now = datetime.now().time()
while True:
    now = datetime.now().time()
    print("Fetching...")
    ryolen_timeline = api.user_timeline(bot_target)
    for i in range(20):
        if ryolen_timeline[i].text[0] != '@':
            last_tweet = ryolen_timeline[i]
            break
    print("Last tweet: {}".format(last_tweet.text))
    if debug or time(0, 0) <= now and now <= time(4, 0):
        if "จะไปนอนแล้ว" in last_tweet.text:
            print("Finally.")
            exit()
        if last_tweet.id != replied_tweet_id:
            replied_tweet_id = last_tweet.id
            print('Reply!')
            try:
                api.update_status(
                    "@{} {}".format(bot_target, get_text()),
                    in_reply_to_status_id = replied_tweet_id
                )
            except:
                pass
            f = open('last_tweet_id.txt', 'w')
            f.write(str(replied_tweet_id))
            f.close()
    sleep(80)
print("Exited.")
