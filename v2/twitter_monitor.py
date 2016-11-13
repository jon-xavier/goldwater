import threading
import json
from twython import TwythonStreamer

from v2.config import consumer_key, consumer_secret, access_token, access_secret

class HashtagStreamer(TwythonStreamer):

    streamer_hashtag = ''
    counter = 60

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret, hashtag):
        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.streamer_hashtag = hashtag
        try:
            f = open('{}.json'.format(self.streamer_hashtag))
        except FileNotFoundError:
            open('{}.json'.format(self.streamer_hashtag), 'w')


    def on_success(self, data):
        self.counter = 60
        if data.get('retweeted_status', None) is None:

            with open('{}.json'.format(self.streamer_hashtag), 'a') as file:
                encoded_string = json.dumps(data)
                file.write('{}\n'.format(encoded_string))
        print(self.streamer_hashtag)
        print(data)

    def on_error(self, status_code, data):
        if status_code == '420':
            time.sleep(self.counter)
            counter = self.counter*2
        print(status_code)
        print(data)


def create_stream(hashtag):
    stream = HashtagStreamer(consumer_key, consumer_secret, access_token, access_secret, hashtag)
    print('created listener for {}'.format(stream.streamer_hashtag))
    stream.statuses.filter(track=stream.streamer_hashtag)

if __name__ == '__main__':

    with open('hashtags.txt', 'r') as f:
        hashtags_to_crawl = list(map(lambda x: x.strip(), f.readlines()))

    threads = []
    print(hashtags_to_crawl)
    for hashtag in hashtags_to_crawl:
        print(hashtag)
        t = threading.Thread(target=create_stream, args=(hashtag, ))
        threads.append(t)

    for thread in threads:
        print('starting thread')
        thread.start()

    #stream.statuses.filter(track="#tcot")

