from enum import Enum
from random import randrange


class GameStatus(Enum):
    WON = 1
    LOST = 2
    IN_PROGRESS = 3
    NOT_STARTED = 4


class Game:
    def __init__(self, allowed_misses: int = 6):
        # if allowed_misses < 1000 or allowed_misses > 8:
        #   raise ValueError("Number of misses should be between 5 and 8")
        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__words = []
        self.__word = ''

    def generate_word(self):
        while self.game_status == GameStatus.NOT_STARTED:
            filename = r'C:\Users\User\PycharmProjects\first_project\files\original.txt'
            words = []
            with open(filename, encoding='utf-8', mode='r+') as file:
                for line in file:
                    words.append(line.strip('\n'))
            self.words = words
            random_index = randrange(0, len(self.words))
            self.word = self.words[random_index]
            # print('Help:', self.word, end='\n')
            self.game_status = GameStatus.IN_PROGRESS

    def give_letter(self, letter: str):
        if len(letter) == 1 and self.game_status == GameStatus.IN_PROGRESS and self.tries_counter < self.allowed_misses:
            if (self.word.find(letter) != -1) and (self.tried_letters.count(letter) == 0):
                self.tried_letters.append(letter)
                temp = self.word
                while temp.find(letter) != -1:
                    self.open_indexes.append(temp.find(letter))
                    index = temp.find(letter)
                    temp = temp[:index] + '*' + temp[index + 1:]
            elif letter != '' and self.tried_letters.count(letter) != 0:
                print(f"Буква {letter} уже отгадана")
            else:
                self.tries_counter += 1
                if self.tries_counter >= self.allowed_misses:
                    self.game_status = GameStatus.LOST
                    return
            self.show_game_status()
        else:
            print('Введите одну букву а не несколько')

    def show_game_status(self):
        flag = True
        print(f'Letter({len(self.word)}): |', end='')
        for i in range(len(self.word)):
            if self.open_indexes.count(i) != 0:
                print(self.word[i], end='|')
            else:
                flag = False
                print('*', end='|')
        if flag:
            self.game_status = GameStatus.WON
        else:
            self.client_tries()

    def client_tries(self):
        print(f'\nКоличество попыток:{self.allowed_misses - self.tries_counter}')

    def client_tried_letters(self):
        return sorted(self.tried_letters)

    # All Properties

    # __allowed_misses
    def get_allowed_misses(self):
        return self.__allowed_misses

    allowed_misses = property(get_allowed_misses)

    # __tries_counter
    def get_tries_counter(self):
        return self.__tries_counter

    def set_tries_counter(self, value):
        self.__tries_counter = value

    tries_counter = property(get_tries_counter, set_tries_counter)

    # __tried_letters
    def get_tried_letters(self):
        return self.__tried_letters

    def set_tried_letters(self, value):
        self.__tried_letters = value

    tried_letters = property(get_tried_letters, set_tried_letters)

    # __open_indexes
    def get_open_indexes(self):
        return self.__open_indexes

    open_indexes = property(get_open_indexes)

    # __game_status
    def get_game_status(self):
        return self.__game_status

    def set_game_status(self, value):
        self.__game_status = value

    game_status = property(get_game_status, set_game_status)

    # __words
    def get_words(self):
        return self.__words

    def set_words(self, value):
        self.__words = value

    words = property(get_words, set_words)

    # __word
    def get_word(self):
        return self.__word

    def set_word(self, value):
        self.__word = value

    word = property(get_word, set_word)


if __name__ == '__main__':
    game = Game(100)
    game.generate_word()
    game.show_game_status()
    while game.game_status != GameStatus.WON and game.game_status != GameStatus.LOST:
        choice = input('Введите букву для отгадки = ')
        try:
            num = int(choice)
            print('Введите букву..., а не цифру')
        except:
            if 'а'.encode('utf-8') <= choice.encode('utf-8') <= 'я'.encode('utf-8'):
                game.give_letter(choice.lower())
            else:
                print('Введите русские буквы')
    if game.game_status == GameStatus.WON:
        # print('\n', game.client_tried_letters())
        print('\nYou WON!')
    elif game.game_status == GameStatus.LOST:
        print('\nYou LOST!')
        print('Загаданное слово:', game.word)
