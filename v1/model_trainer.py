class ModelTrainer():
    def __init__(self, training_set):
        self.lowercase(training_set)
        self.word_frequency_dict = self.train_word_frequency(training_set)

    def lowercase(self, training_set):
        with open('{}.txt'.format(training_set), 'r') as f:
            text = str(f.read()).lower()
        with open('{}.txt'.format(training_set), 'w') as f:
            f.write(text)

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
        pass


if __name__ == '__main__':
    tcot = ModelTrainer('#tcot')
    tmp =''
    for key, value in tcot.word_frequency_dict.items():
        tmp += '{}\n'.format(str(key))
        tmp += '{}\n'.format(str(value))
    with open('tcot_finished_model.txt', 'w') as m:
        m.write(tmp)
