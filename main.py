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


dc = {
    'kids': [float('inf'), 5],
    'easy': [8, 5],
    'classic': [6, 5],
    'hard': [6, 7]
}


def menu():
    print('Welcome to Wordle! ')
    levels = ['kids', 'easy', 'classic', 'hard']
    choice = None
    while choice != 'no':
        print('Choose one from following levels, or type exit to quit')
        print(*levels, sep='\n')
        lvl = input('Enter lvl: ')
        if lvl == 'exit':
            break
        if lvl not in levels:
            print('level does not exists! choose the right one')
            continue
        selected_lvl = dc.get(lvl)
        g = Game(*selected_lvl)
        while g.count < g.tries:
            guessed_word = input('\nGuess the word: ').lower()
            if len(guessed_word) != selected_lvl[1]:
                print(f'Enter word with {selected_lvl[1]} letters')
                continue
            response = g.gameplay(guessed_word)
            print('\n', response)
            if response != 'wrong word':
                break
        choice = input('Do you want to play again?: ')
        if choice not in ['yes', 'no']:
            continue


if __name__ == '__main__':
    menu()
