import time
import led_strip
import notable_tweet
import json

with open('credentials.secret') as json_data_file:
    config = json.load(json_data_file)
print("API Key", config['twitter_app_credentials']['APIKey'])
print("API Secret", config['twitter_app_credentials']['APISecret'])
print("Access Token", config['twitter_app_credentials']['AccessToken'])
print("Token Secret", config['twitter_app_credentials']['AccessTokenSecret'])

# LED strip configuration:
LED_COUNT = 180  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

tweet_strip = led_strip.LedStripControl(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

colours = [led_strip.rpi_ws281x.Color(255, 0, 0),
           led_strip.rpi_ws281x.Color(255, 0, 0),
           led_strip.rpi_ws281x.Color(255, 255, 0),
           led_strip.rpi_ws281x.Color(0, 255, 0),
           led_strip.rpi_ws281x.Color(0, 0, 255)]

tweet_strip.pixel_clear()

time.sleep(4)

tweet_strip.set_strip_colours(colours)



consumer_key = "L0ZMAJxYVbWinZtbSy3ph69dy"
consumer_secret = "27BVyFWrfGGWz5VLQc5CdqLYdNtVuPHNPGemzgQSRtVF4lnukS"
access_token = "1635348644-5D2pogpmyUh20XIxFtMcYoNVCQPL958HCkyJqLv"
access_token_secret = "ynKirsuvYqxdT5LzUNSLLlidX4dfkdoFPDDVTBjVG51aP"

notable_tweet_list = []
notable_screen_names = []



tweet_processor = notable_tweet.TweetPocessor(
                  config['twitter_app_credentials']['APIKey'],
                  config['twitter_app_credentials']['APISecret'],
                  config['twitter_app_credentials']['AccessToken'],
                  config['twitter_app_credentials']['AccessTokenSecret'],
                  notable_screen_names, notable_tweet_list)

myStream = tweepy.Stream(auth=tweet_processor.api.auth, listener=tweet_processor)
