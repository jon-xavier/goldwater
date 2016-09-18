import threading
import time
import tweepy


from v2.config import consumer_key, consumer_secret, access_token, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter = tweepy.API(auth)

class Hashtag_File:
    filename = ""
    hashtags = set([])

    def __init__(self, filename):
        hashtags = self.read_hashtags(filename)
        self.filename = filename
        self.hashtags = set(hashtags)

    def read_hashtags(self, filename):
        with open(filename, 'r') as f:
            hashtags = map(lambda x: x.strip(), f.readlines())
        return hashtags

    def new_hashtags(self):
        current_hashtags = set(self.read_hashtags(self.filename))
        new = current_hashtags - self.hashtags
        self.hashtags = current_hashtags
        return new

    def return_hashtags(self):
        self.read_hashtags()
        return self.hashtags


class HashtagMonitor(threading.Thread):
    def __init__(self, hashtag_filename):
        threading.Thread.__init__(self)
        self.active_file = Hashtag_File(hashtag_filename)
        self.stop_thread = False
        self.last_query = set([])

    def run(self):
        while not self.stop_thread:
            current_hashtags = self.active_file.read_hashtags()
            if len(current_hashtags) >= len(self.last_query):
                new_hashtags = self.active_file.new_hashtags()

        self.last_query = set(current_hashtags)



class QueryTwitter:


class TrainingSetUpdater:


def main():


if __name__ = "__main__":
    main()

