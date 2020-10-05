from enum import Enum
from random import randrange


class GameStatus(Enum):
    WON = 1
    LOST = 2
    IN_PROGRESS = 3
    NOT_STARTED = 4


class Game:
    def __init__(self, allowed_misses: int = 6, file_path: str = r'..\files\original.csv'):
        # вопрос - ответ - объяснение
        self.file_path = file_path
        self.dict = {'y': 'Yes', 'n': 'No', 'Y': 'Yes', 'N': 'No', 'yes': 'Yes', 'no': 'No', 'Yes': 'Yes', 'No': 'No',
                     'да': 'Yes', 'нет': 'No', 'Да': 'Yes', 'Нет': 'No'}
        self.allowed_misses = allowed_misses
        self.tries_counter = 0
        self.questions = []
        self.counter = 1
        self.answers = []
        self.client_answers = {}
        self.explanations = []
        self.used_index = []
        self.game_status = GameStatus.NOT_STARTED

    def get_data(self):
        with open(self.file_path, 'r+') as file:
            for line in file:
                temp = line.strip('\n')
                questions, answers, explanation = temp.split(';')
                self.questions.append(questions)
                self.answers.append(answers)
                self.explanations.append(explanation)
                self.game_status = GameStatus.IN_PROGRESS
            print(f"We have {len(self.questions)} questions")

    def get_question(self):
        if self.game_status == GameStatus.IN_PROGRESS and self.tries_counter < self.allowed_misses:
            while True:
                random_index = randrange(0, len(self.questions))
                if self.used_index.count(random_index) == 0:
                    self.used_index.append(random_index)
                    break
                else:
                    continue
            print(f'Tries left: {self.allowed_misses - self.tries_counter}')
            print(f'Question({self.counter}):{self.questions[random_index]}')
            self.counter += 1
            answer = input('Answer[y/n]:')
            self.client_answers.update({random_index: self.dict[answer]})
            if self.check_answer(random_index):
                print('Right!')
            else:
                self.tries_counter += 1
                print('You\'r Wrong!')
                print(f'Explanation:{self.explanations[random_index]}')
        else:
            self.game_status = GameStatus.LOST

    def check_answer(self, index):
        if len(self.client_answers) == len(self.answers) and self.answers[index] == self.client_answers[index]:
            self.game_status = GameStatus.WON
        if self.answers[index] == self.client_answers[index]:
            return True
        return False

    @staticmethod
    def get_status():
        return game.game_status


if __name__ == '__main__':
    game = Game()
    game.get_data()
    while game.game_status != GameStatus.LOST and game.game_status != GameStatus.WON:
        game.get_question()
    if game.game_status == GameStatus.LOST:
        print("You LOST!")
    elif game.game_status == GameStatus.WON:
        print("You WON!")
