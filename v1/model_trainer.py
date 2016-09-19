class ModelTrainer():
    def __init__(self, training_set):
        self.word_frequency_dict = self.train_word_frequency(training_set)

    def train_word_frequency(self, training_set):
        tweets = []
        model = {}
        with open("{}.txt".format(training_set) , 'r') as t:
            tweets = [line.strip() for line in t]


        for tweet in tweets:
            words = tweet.split()
            for word in words:
                model[word] = model.get(word, 0) + 1

        for key in model.keys():
            model[key] = model[key] / sum(model.values())

        return model

    def train_markov_model(self):
        

if __name__ == '__main__':
    tcot = ModelTrainer()
    finished_model = tcot.train_word_frequency('#tcot')
    for key in finished_model.keys():
        print(key)
        print(finished_model[key])
