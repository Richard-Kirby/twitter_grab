import datetime
import tweepy
import re
import colorsys

class Tweeter:

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


    def check_tweet(self, tweet):
        #print("tweet check", tweet.text)
        if self.tweet_re.match(tweet.text) is not None:
            print("tweet>>", self.name,self.count, self.colour)
            self.count = self.count+1
            ret_colour = self.colour
        elif self.retweet_re.match(tweet.text) is not None:
            self.re_count = self.re_count +1
            ret_colour = self.colour
            print("<<retweet", self.name, self.re_count, ret_colour)
        else:
            ret_colour = None
        return ret_colour


# override tweepy.StreamListener to add logic to on_status
class TweetPocessor(tweepy.StreamListener):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, notable_tweeters,
                 notable_tweet_list):

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        print("Setup up API")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        tweepy.StreamListener.__init__(self, api=self.api)

        self.tweeters =[]

        for tweeter in notable_tweeters["tweeters"]:
            new_tweeter = Tweeter(tweeter)
            #print (new_tweeter)
            self.tweeters.append(new_tweeter)

        self.notable_tweet_list = notable_tweet_list

    def on_status(self, status):
        #print(status.id, status.created_at, status.author.screen_name, status.text)

        for tweeter in self.tweeters:
            ret_colour = tweeter.check_tweet(status)
            if ret_colour is not None:
                #print(ret_colour)
                self.notable_tweet_list.append(ret_colour)


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
