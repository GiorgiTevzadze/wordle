import random
from termcolor import colored


class Game:
    def __init__(self, tries, characters):
        self.words = open('/home/unn/Desktop/ka_GE.txt')
        self.count = 0
        self.words_list = [word.split(' ')[0] for word in self.words if len(word.split(' ')[0]) == characters]
        self.tries = tries
        self.random_word = random.choice(self.words_list)

    def gameplay(self, guessed_word):
        self.count += 1
        if guessed_word == self.random_word:
            return f'you won with {self.count} try. Guessed word was {self.random_word}'
        elif self.count >= self.tries:
            return f'You lost. Guessed word was {self.random_word}'
        for i in range(min(len(guessed_word), self.tries)):
            if guessed_word[i] == self.random_word[i]:
                print(colored(guessed_word[i], 'green'), end="")
            elif guessed_word[i] in self.random_word:
                print(colored(guessed_word[i], 'yellow'), end="")
            else:
                print(guessed_word[i], end='')
        if not isinstance(self.tries, float):
            print(f'\nYou have left {self.tries - self.count} trie')
        return 'wrong word'