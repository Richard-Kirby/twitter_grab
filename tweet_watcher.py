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

                    wrap = len(self.notable_tweet_list)// self.led_strip.strip.numPixels()
                    mod = len(self.notable_tweet_list) % self.led_strip.strip.numPixels()
                    print(wrap, ":", mod)

                    mod_list =[]
                    for i in range (self.led_strip.strip.numPixels()):
                        #print(i)
                        if i < mod:
                            colour = self.notable_tweet_list[i]
                        else:
                            colour = (0,0,0)

                        if i < wrap:
                            colour = (colour[0], colour[1], 255)

                        #print (colour)

                        mod_list.append(colour)

                    self.led_strip.set_strip_colours(mod_list)

                time.sleep(4)

        except KeyboardInterrupt:
            print("closing")
        except:
            raise
