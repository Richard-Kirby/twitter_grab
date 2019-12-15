import datetime
import tweepy
import re
import colorsys


# Class for each tweeter that is being followed.  Knows how to check for tweets or re-tweets.
class Tweeter:

    # Set up reg exs, colours, etc.
    def __init__(self, tweeter_info):
        self.name = tweeter_info["name"]
        self.id = tweeter_info["id"]
        self.colour = colorsys.hsv_to_rgb(float(tweeter_info["hue"]), float(tweeter_info["sat"]), float(tweeter_info["val"]))
        self.colour = (int(self.colour[0] * 255), int(self.colour[1] * 255), int(self.colour[2] * 255))

        tweet_string_re = "^" + self.name+ ".*"
        print(tweet_string_re)
        self.tweet_re = re.compile(tweet_string_re)
        retweet_string_re = ".*RT.*" + self.name + ".*"

        print(retweet_string_re)
        self.retweet_re = re.compile(retweet_string_re)
        self.re_count = 0
        self.count = 0

    # Checks the tweet against its own name to see if a tweet or re-tweet.
    def check_tweet(self, tweet):
        #print("tweet check", tweet.text)

        # Check against the two regexes looking for tweet.
        if self.tweet_re.match(tweet.text) is not None:
            print("tweet>>", self.name,self.count, self.colour)
            self.count = self.count+1
            ret_value = 'tweet'

        # As above re-tweet check
        elif self.retweet_re.match(tweet.text) is not None:
            self.re_count = self.re_count +1
            ret_value = 're-tweet'
            print("<<retweet", self.name, self.re_count, self.colour)

        # None value - is not my tweet or re-tweet.
        else:
            ret_value = None
        return ret_value


# override tweepy.StreamListener to add logic to on_status.  Sets everything up and gets the tweets processed.
class TweetPocessor(tweepy.StreamListener):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, notable_tweeters,
                 notable_tweet_list):

        # Setting up the API as per standard Tweepy process.
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        tweepy.StreamListener.__init__(self, api=self.api)

        # Build the list of tweeters being watched.
        self.tweeters =[]

        for tweeter in notable_tweeters["tweeters"]:
            new_tweeter = Tweeter(tweeter)
            #print (new_tweeter)
            self.tweeters.append(new_tweeter)

        self.notable_tweet_list = notable_tweet_list

    # This gets run whenever a new tweet comes in.  It figures out who tweeted or was re-tweeted.
    def on_status(self, status):
        #print(status.id, status.created_at, status.author.screen_name, status.text)

        #Pass the tweet to the object so it can check if it is one its tweets involved.
        for tweeter in self.tweeters:
            tweet_or_re_tweet = tweeter.check_tweet(status)

            # Check the return value of the tweet check.  Add the tweeter to the list of tweets if
            # tweeted or re-tweeted.
            if tweet_or_re_tweet is not None:
                #print(ret_colour)
                self.notable_tweet_list.append(tweeter)


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
