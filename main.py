# external imports
import time
import threading
import json
import tweepy
import tweet_watcher


# Project imports
import led_strip
import notable_tweet

# LED strip configuration:
LED_COUNT = 180 # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)


# Grab the credentials.
with open('credentials.secret') as json_data_file:
    config = json.load(json_data_file)

# Grab the twitter ids we are interested in.
with open('notable_tweeters') as json_data_file:
    notable_tweeters = json.load(json_data_file)

# Build a list of notable IDs to follow from the JSON file
notable_ids = []
for tweeter in notable_tweeters["tweeters"]:
    notable_ids.append(tweeter["id"])

notable_tweet_list = []

# Initialise the tweet processor - this deals with the stream.
tweet_processor = notable_tweet.TweetPocessor(
                  config['twitter_app_credentials']['APIKey'],
                  config['twitter_app_credentials']['APISecret'],
                  config['twitter_app_credentials']['AccessToken'],
                  config['twitter_app_credentials']['AccessTokenSecret'],
                  notable_tweeters, notable_tweet_list)

# Set up the twitter stream, uses the processor created above.
myStream = tweepy.Stream(auth=tweet_processor.api.auth, listener=tweet_processor)

# Set up the neo-pixel strip for use by the twitter analyser
tweet_strip = led_strip.LedStripControl(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
tweet_strip.pixel_clear()

# Set up the watcher thread.  This deals with the output from the tweet processor.
tweet_watcher_thread = tweet_watcher.TweetWatcher(notable_tweet_list, tweet_strip)
tweet_watcher_thread.start()

# Specify the filter for the stream.
myStream.filter(follow=notable_ids)
