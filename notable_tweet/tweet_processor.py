import datetime
import tweepy
import re

# override tweepy.StreamListener to add logic to on_status
# class MyStreamListener(tweepy.StreamListener):
#
#    def on_status(self, status):   
#       print(status.text)


class TweetPocessor(tweepy.StreamListener):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, notable_tweeters,
                 notable_tweet_list):

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        print("Setup up API")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        tweepy.StreamListener.__init__(self, api=self.api)

        self.seth_count = 0
        self.seth_re_count = 0

        self.last_tweet = None

        self.seth = re.compile('^SethAbramson.*')
        self.seth_re = re.compile('.*RT\s*@SethAbramson.*')

        self.notable_tweet_list = notable_tweet_list

    def on_status(self, status):
        #print(status.id, status.created_at, status.author.screen_name, status.text)

        if self.seth.match(status.text) is not None:
            self.seth_count = self.seth_count +1
            print("count", self.seth_count)

            tweet_colour = (0,50,0)
            self.notable_tweet_list.append(tweet_colour)

        if self.seth_re.match(status.text) is not None:
            self.seth_re_count = self.seth_re_count +1
            print("re tweet", self.seth_re_count)

            tweet_colour = (50,0,0)
            self.notable_tweet_list.append(tweet_colour)

'''
    def grab_tweets(self):

        while (1):
            print("Grab Tweets", datetime.datetime.now())

            if self.last_tweet is None:

                public_tweets = self.api.home_timeline()

            else:
                public_tweets = self.api.home_timeline(since_id=self.last_tweet)

            if public_tweets is not None:
                for tweet in public_tweets:
                    # print(tweet.id, ": ", tweet.author.screen_name, ": ", tweet.created_at , ": ", tweet.text)
                    print(tweet.id, tweet.created_at, tweet.author.screen_name, tweet.full_text)

            self.last_tweet = tweet.id
'''

if __name__ == "__main__":
    notable_screen_names = []
    notable_tweet_list = []

    tweet_processor = TweetPocessor(consumer_key, consumer_secret, access_token, access_token_secret,
                                    notable_screen_names, notable_tweet_list)

    myStream = tweepy.Stream(auth=tweet_processor.api.auth, listener=tweet_processor)

    print(myStream)

    print(notable_ids)
    myStream.filter(follow = notable_ids)

    print(myStream)
    #myStream.filter(track=['Trump'])


    # tweet_processor.grab_tweets()
