import threading
import time


# Class that watches the Tweet list and gets them displayed in the LED strip.
class TweetWatcher(threading.Thread):

    # Set up the accelerometer.  Power and sensitivity settings
    def __init__(self, notable_tweet_list, led_strip):

        # Initialise the Thread.
        threading.Thread.__init__(self)
        self.notable_tweet_list = notable_tweet_list
        self.led_strip = led_strip

    def run(self):

        last_len = 0
        last_tweeter_display = 0
        try:
            mod_list = []

            while True:

                # Check is length of notable tweets have changed.
                curr_len = len(self.notable_tweet_list)
                if curr_len > last_len:
                    #print(self.notable_tweet_list)

                    # Figure out the wrapping.
                    wrap = len(self.notable_tweet_list)// self.led_strip.strip.numPixels()
                    mod = len(self.notable_tweet_list) % self.led_strip.strip.numPixels()
                    #print(wrap, ":", mod)

                    # This slices out the mod (gets the last tweets after the wrap)
                    mod_list = self.notable_tweet_list[-mod:]

                    #print("mod list length ", len(mod_list))

                    self.led_strip.set_strip_colours(mod_list)
                    last_len = len(self.notable_tweet_list)

                time.sleep(0.2)

                self.led_strip.set_strip_colours(mod_list)

                # Pause to summarise if list is a multiple of 50
                summarise_calc = len(self.notable_tweet_list) // 50

                if summarise_calc > last_tweeter_display: # self.led_strip.strip.numPixels():
                    tweeters = set(mod_list)
                    for tweeter in tweeters:
                        self.led_strip.set_strip_colours(mod_list, tweeter_filter = tweeter)
                        print("Filter id:{} name:{} count{}:" .format( tweeter.id, tweeter.name, mod_list.count(tweeter)))
                        time.sleep(0.2)

                    last_tweeter_display = summarise_calc

                #time.sleep(0.1)

        except KeyboardInterrupt:
            print("closing")
        except:
            raise
