import tweepy
import time
import collections
import datetime

consumer_key = "L0ZMAJxYVbWinZtbSy3ph69dy"
consumer_secret = "27BVyFWrfGGWz5VLQc5CdqLYdNtVuPHNPGemzgQSRtVF4lnukS"
access_token = "1635348644-5D2pogpmyUh20XIxFtMcYoNVCQPL958HCkyJqLv"
access_token_secret = "ynKirsuvYqxdT5LzUNSLLlidX4dfkdoFPDDVTBjVG51aP"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print("Setup up API")
api = tweepy.API(auth, wait_on_rate_limit=True)
last_tweet = None

print("Grab Tweets")
public_tweets = api.home_timeline()
last_tweet = None

tweet_tuple = collections.namedtuple('tweet_tuple', ['id', 'created_at', 'screen_name', 'text'])

tweet_list = []

notable_screen_name = collections.namedtuple('notable_screen_name', ['screen_name', 'R', 'G', 'B'])

notable_screen_name_list = [['yashar', 0, 255, 255],
                            ['Trump', 255, 0, 0],
                            ['SethAbramson', 0,255, 0]]

print(notable_screen_name_list)


notable_tweet_tuple = collections.namedtuple('notable_tweet_tuple', ['id', 'created_at', 'screen_name', 'text', 'R', 'G', 'B'])
notable_tweet_tuple_list = []



while (1):

    if public_tweets is not None:
        for tweet in public_tweets:
            #print(tweet.id, ": ", tweet.author.screen_name, ": ", tweet.created_at , ": ", tweet.text)
            new_tweet = tweet_tuple(tweet.id, tweet.created_at, tweet.author.screen_name, tweet.text)
            #print(new_tweet)
            #print(new_tweet.screen_name)

            if 'Trump' in new_tweet:
                print("found Trump", new_tweet)
            elif 'yashar'in new_tweet:
                print("found yashar", new_tweet)
            elif new_tweet.screen_name == 'TheRickWilson':
                print("RickWilson Found", new_tweet)
            elif new_tweet.screen_name == 'SethAbramson':
                print("found Seth Abramson", new_tweet)
                new_notable_tweet = new_tweet, notable_screen_name('SethAbramson').R, notable_screen_name('SethAbramson').G, notable_screen_name('SethAbramson').B

                notable_tweet_tuple_list.append( new_notable_tweet)

            # Append the new tweet into the list
            tweet_list.append(new_tweet)

        last_tweet = tweet


    time.sleep(120)

    #print("Grab Tweets")

    if last_tweet is None:

        public_tweets = api.home_timeline()
    else:
        print("Grab next set of Tweets", datetime.datetime.now())
        public_tweets = api.home_timeline(since_id = last_tweet.id)

