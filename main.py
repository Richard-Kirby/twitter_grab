# external imports
import time
import threading
import json
import tweepy
import tweet_watcher


# Project imports
import led_strip
import notable_tweet


with open('credentials.secret') as json_data_file:
    config = json.load(json_data_file)

with open('notable_tweeters') as json_data_file:
    notable_tweeters = json.load(json_data_file)

#print(notable_tweeters)

for each tweeter in notable_tweeters:
    print tweeter.name




#print("API Key", config['twitter_app_credentials']['APIKey'])
#print("API Secret", config['twitter_app_credentials']['APISecret'])
#print("Access Token", config['twitter_app_credentials']['AccessToken'])
#print("Token Secret", config['twitter_app_credentials']['AccessTokenSecret'])

# LED strip configuration:
LED_COUNT = 180 # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

tweet_strip = led_strip.LedStripControl(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

colours = [(255, 0, 0),
           (255, 0, 0),
           (255, 255,0),
           (0, 255, 0),
           (0, 0, 255)]

tweet_strip.pixel_clear()

time.sleep(4)

tweet_strip.set_strip_colours(colours)
notable_tweet_list = []


tweet_processor = notable_tweet.TweetPocessor(
                  config['twitter_app_credentials']['APIKey'],
                  config['twitter_app_credentials']['APISecret'],
                  config['twitter_app_credentials']['AccessToken'],
                  config['twitter_app_credentials']['AccessTokenSecret'],
                  notable_tweeters, notable_tweet_list)

myStream = tweepy.Stream(auth=tweet_processor.api.auth, listener=tweet_processor)

# Set up the watcher thread.  Deals with the active tweetstream.
tweet_watcher_thread = tweet_watcher.TweetWatcher(notable_tweet_list, tweet_strip)
tweet_watcher_thread.start()

myStream.filter(follow=notable_ids)


