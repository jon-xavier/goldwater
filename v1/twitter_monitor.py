import threading
import time
import tweepy

from v1.config import consumer_key, consumer_secret, access_token, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter = tweepy.API(auth)


class Twitter_Crawler():

    def __init__(self, hashtag_filename):
        self.active_file = Hashtag_File(hashtag_filename)
        #self.t = threading._start_new_thread(lambda: self.crawl_hashtags(), ())
        self.t = threading.Thread(target=self.crawl_hashtags)
        self.stop_thread = False
        self.t.start()

    def crawl_hashtags(self):
        while not self.stop_thread:
            current_hashtags = self.active_file.return_hashtags()
            for hashtag in current_hashtags:
                hashfile = "{}.txt".format(hashtag)
                hash_list = twitter.search(hashtag, count=100)
                current_tweets = ""

                with open(hashfile, 'rb') as f:
                    current_tweets = set(f.readlines())

                for tweet in hash_list:
                    if not hasattr(tweet, 'retweeted_status'):
                        text = tweet.text.encode('ascii', 'ignore')
                        if not text in current_tweets:
                            current_tweets.add(text)

                with open(hashfile, 'wb') as f:
                    f.write(b'\n'.join(current_tweets))


            time.sleep(4)
    def stop(self):
        self.stop_thread = True

    def join_thread(self):
        self.t.join()



class Hashtag_File:
    filename = ""
    hashtags = set([])
    def read_hashtags(self, filename):
        with open(filename, 'r') as f:
            hashtags = map(lambda x: x.strip(), f.readlines())
        return hashtags

    def __init__(self, filename):
        hashtags = self.read_hashtags(filename)
        self.filename= filename
        self.hashtags = set(hashtags)

    def update_hashtags(self):
        current_hashtags = set(self.read_hashtags(self.filename))
        new = current_hashtags - self.hashtags
        self.hashtags = current_hashtags
        return new

    def return_hashtags(self):
        self.update_hashtags()
        return self.hashtags

test = Twitter_Crawler('hashtags.txt')
test.stop()
test.join_thread()



