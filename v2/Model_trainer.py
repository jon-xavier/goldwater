import json


class Model_Trainer():
    def __init__(self, hashtag):
        self.training_set = []
        with open('{}.json'.format(hashtag), 'r') as f:
            for line in f:
                current_line = json.loads(line)
                self.training_set.append(current_line)

if __name__ == '__main__':
    tcot = Model_Trainer('#tcot')
    for tweet in tcot.training_set:
        print(tweet['text'])
