import threading
import time


class TweetWatcher(threading.Thread):

    # Set up the accelerometer.  Power and sensitivity settings
    def __init__(self, notable_tweet_list, led_strip):

        # Initialise the Thread.
        threading.Thread.__init__(self)
        self.notable_tweet_list = notable_tweet_list
        self.led_strip = led_strip

    def run(self):

        last_len = 0
        try:
            while (1):
                if len(self.notable_tweet_list) > last_len:
                    #print(self.notable_tweet_list)
                    self.led_strip.set_strip_colours(self.notable_tweet_list)
                time.sleep(4)

        except KeyboardInterrupt:
            print("closing")
        except:
            raise
