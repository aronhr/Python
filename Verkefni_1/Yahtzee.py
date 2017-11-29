# Global Imports
import random

# Class Definitions
class Score(object):
    def __init__(self):
        self.dict = createDefaultDict()

    def total(self):
        total = 0
        for item in self.dict.values():
            total += item
        return total

    def update(self, row, new_score):
        self.dict[row] = new_score

    def bonus_check(self):
        top_total = 0
        for i in range(1, 7):
            top_total += self.dict[str(i)]
        if top_total >= 63:
            self.dict['bon'] = 35

    def calc(self, scored_row):
        roll_score = 0
        counter = 0

        # Prevents player from double-scoring
        while score.dict[scored_row]:
            if scored_row == 'yat' and score.dict['yat'] > 1 and \
            dice.dice.count(dice.dice[1]) == 5:
                break
            print("You've already scored that row." + dice.message)
            scored_row = get_input()

        # Prevents player from self-scoring Bonus
        while scored_row == 'bon':
            print('Invalid choice.' + dice.message)
            scored_row = get_input()

        # Logic for rows 1 - 6
        if scored_row in str(range(1, 7)):
            if scored_row not in dice.dice:
                roll_score = 1
            else:
                for die in dice.dice:
                    if die == scored_row:
                        counter += 1
                roll_score = int(scored_row) * counter
            self.update(scored_row, roll_score)
            return

        # Logic for 3k
        if scored_row == '3k':
            for die in dice.dice:
                if dice.dice.count(die) >= 3:
                    counter = 1
            if not counter:
                roll_score = 1
            if counter:
                roll_score = dice.total()
            self.update(scored_row, roll_score)
            return

        # Logic for 4k
        if scored_row == '4k':
            for die in dice.dice:
                if dice.dice.count(die) >= 4:
                    counter = 1
            if not counter:
                roll_score = 1
            if counter:
                roll_score = dice.total()
            self.update(scored_row, roll_score)
            return

        # Logic for Small Straight
        if scored_row == 'sm':
            dice_copy = dice.dice
            dice_copy.sort()
            poss = '1 2 3 4'.split(), '2 3 4 5'.split(), '3 4 5 6'.split()
            roll_score = 1
            for i in range(0, 7):
                if dice_copy.count(str(i)) >= 2:
                    dice_copy.remove(str(i))
            if (dice_copy[1:5] in poss) or (dice_copy[2:] in poss):
                roll_score = 30
            self.update(scored_row, roll_score)
            return

        # Logic for Large Straight
        if scored_row == 'lg':
            dice_copy = dice.dice
            dice_copy.sort()
            poss = '1 2 3 4 5'.split(), '2 3 4 5 6'.split()
            roll_score = 1
            if dice_copy[1:] in poss:
                roll_score = 40
            self.update(scored_row, roll_score)
            return

        # Logic for Full House
        if scored_row == 'fh':
            dice_copy = dice.dice
            dice_copy.sort()
            roll_score = 1
            for i in range(1, 6):
                if dice.dice.count(str(i)) not in (0, 2, 3):
                    roll_score = 1
                    break
                elif 1 < dice.dice.count(str(i)) < 4:
                    roll_score = 25
            self.update(scored_row, roll_score)
            return

        # Logic for Yahtzee
        if scored_row == 'yat':
            roll_score = 50
            if dice.dice.count(dice.dice[1]) != 5:
                roll_score = 1
            if self.dict['yat'] > 2:
                roll_score = self.dict['yat']
                roll_score += 100
            self.update(scored_row, roll_score)
            return

        # Logic for Chance
        if scored_row == 'ch':
            roll_score = dice.total()
            self.update(scored_row, roll_score)
            return


class Board(object):
    def __init__(self):
        self.isNotComplete = True

    #@staticmethod
    def display(self):
        print('Y A H T Z E E'.center(21))
        print('+---+---+  +---+---+')
        print('|  1|' + str(score.dict['1']).center(3) + '|  | 3k|' + str(score.dict['3k']).center(3) + '|')
        print('+---+---+  +---+---+')
        print('|  2|' + str(score.dict['2']).center(3) + '|  | 4k|' + str(score.dict['4k']).center(3) + '|')
        print('+---+---+  +---+---+')
        print('|  3|' + str(score.dict['3']).center(3) + '|  | FH|' + str(score.dict['fh']).center(3) + '|')
        print('+---+---+  +---+---+')
        print('|  4|' + str(score.dict['4']).center(3) + '|  | Sm|' + str(score.dict['sm']).center(3) + '|')
        print('+---+---+  +---+---+')
        print('|  5|' + str(score.dict['5']).center(3) + '|  | Lg|' + str(score.dict['lg']).center(3) + '|')
        print('+---+---+  +---+---+')
        print('|  6|' + str(score.dict['6']).center(3) + '|  |Yat|' + str(score.dict['yat']).center(3) + '|')
        print('+===+===+  +---+---+')
        print('|Bon|' + str(score.dict['bon']).center(3) + '|  | Ch|' + str(score.dict['ch']).center(3) + '|')
        print('+===+===+  +===+===+')


class Dice(object):
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]
        self.roll_counter = 0
        self.held = []
        self.message = ''

    def display(self):
        for item in self.dice[1:]:
            print(item),
        currently_held = [' ', 'H', 'H', 'H', 'H', 'H']
        for i in range(0, 6):
            if str(i) not in self.held:
                currently_held[i] = ' '
        for item in currently_held:
            print(item),

        if dice.roll_counter == 3:
            self.message = "Enter your desired score row."
            print(self.message)
        elif dice.roll_counter == 0:
            self.message = "Enter 'r' to roll."
            print(self.message)
        else:
            self.message = "Enter the numbers of the dice you would like to hold/release (or 'r') to roll."
            print(self.message)

    def hold(self, keepers):
        for die in keepers:
            if die in self.held:
                self.held.remove(die)
            else:
                self.held.append(die)

    def reset(self):
        self.__init__()

    def roll(self):
        self.roll_counter += 1
        for die in range(1, 6):
            if str(die) in self.held:
                pass
            else:
                self.dice[die] = str(random.randint(1, 6))

    #@staticmethod
    def total(self):
        dice_total = 0
        for die in dice.dice:
            dice_total += int(die)
        return dice_total

# Functions
def cls():
    print('\n' * 25)

def createDefaultDict():
    score_rows = '1 2 3 4 5 6 Bon 3k 4k FH Sm Lg Yat Ch'.split()
    template = {}

    for item in score_rows:
        template[str(item).lower()] = 0
    return template

def get_input():
    while True:
        isvalid = False
        user_choice = input('> ')
        if dice.roll_counter < 3 and user_choice.lower().startswith('r'):
            isvalid = True
        elif dice.roll_counter == 3 and user_choice.lower() in score.dict.keys():
            user_choice = user_choice.lower()
            isvalid = True
        elif 0 < dice.roll_counter < 3 and user_choice.isdigit() and len(user_choice) < 6:
            isvalid = True
            for item in user_choice:
                if item not in str(range(1, 6)) or user_choice.count(item) > 1:
                    isvalid = False
                    break

        if isvalid:
            return user_choice
        else:
            print('Invalid choice.'),
            print(dice.message)

# Game Start
cls()
board = Board()
score = Score()
dice = Dice()
rolls = 0

while True:
    cls()
    board.display()
    if board.isNotComplete:
        dice.reset()
        rolls += 1
        while dice.roll_counter < 4:
            dice.display()
            choice = get_input()
            if dice.roll_counter == 3:
                score.calc(choice)
                if rolls >= 13:
                    board.isNotComplete = False
                    rows_to_check = '1 2 3 4 5 6 3k 4k sm lg fh ch'.split()
                    for row in rows_to_check:
                        if score.dict[row] == 0:
                            board.isNotComplete = True
                if not board.isNotComplete:
                    score.bonus_check()
                break
            if choice.lower().startswith('r'):
                dice.roll()
            else:
                dice.hold(choice)
                dice.roll()

    else:
        print('Congratulations! Your Final score was %s.' % score.total()),
        print('Would you like to play again? (y/n)')
        play_again = input('> ')
        if play_again.lower().startswith('y'):
            score.__init__()
            dice.__init__()
            board.isNotComplete = True
        else:
            break
