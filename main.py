import random


class Game:
    def __init__(self, tries, characters):
        self.words = open('/home/unn/Desktop/ka_GE.txt')
        self.count = 0
        self.words_list = [word.split(' ')[0] for word in self.words if len(word.split(' ')[0]) == characters]
        self.tries = tries
        self.random_word = random.choice(self.words_list)
