import random

class Board:
    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.board_state = []
        self.board_evaluations = []
        self.board_won = 0

    def generate(self):
        if self.difficulty==0:
            self.__solution = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
        else:
            self.__solution = [random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8)]

    def show_solution(self):
        return self.__solution

    def make_guess(self,guess):
        self.board_state.append(guess)
        print(len(self.board_state))
        temp_board_evaluation = []
        checked = [False,False,False,False]

        #checking for all the correct guesses
        if guess[0] == self.__solution[0]:
            checked[0] = True
            temp_board_evaluation.append(9)
        if guess[1] == self.__solution[1]:
            checked[1] = True
            temp_board_evaluation.append(9)
        if guess[2] == self.__solution[2]:
            checked[2] = True
            temp_board_evaluation.append(9)
        if guess[3] == self.__solution[3]:
            checked[3] = True
            temp_board_evaluation.append(9)

        #checking for all the not correct but present  guesses
        for count_guess in range(0,4):#number needed for indexing the checked numbers
            if self.__solution.count(guess[count_guess]) > 0:#if guess is present in the solution
                for current_solution in self.__solution:
                    if guess[count_guess] == current_solution and not checked[count_guess]:#if guess is in the correct position and the current guess has not been used to check a different answer
                        temp_board_evaluation.append(10)
                        checked[count_guess] = True

        #incase no guesses where correct
        if not temp_board_evaluation:
            temp_board_evaluation = [0,0,0,0]

        #filling up tempBoardEvaluations with 0 until its at 4 numbers
        for count_fill in range(len(temp_board_evaluation),4):
            temp_board_evaluation.append(0)

        #check if game is wone
        if guess == self.__solution:
            self.board_won = 1

        #check if game is already lost before adding a guess
        if self.board_won == 0:
            self.board_evaluations.append(temp_board_evaluation)

        #check if board is lost after this guess
        if len(self.board_evaluations) == 9 and self.board_won != 1:
            self.board_won = -1

    def give_row(self,row):
        if row<len(self.board_state):
            return self.board_state[row]
        else:
            return [0,0,0,0]

    def give_board(self):
        return self.boardState

    def give_evaluation(self,row):
        if row<len(self.board_evaluations):
            return self.board_evaluations[row]
        else:
            return [0,0,0,0]

    def give_boardstare(self):
        return self.board_won

    def give_current_row(self):
        return len(self.board_state)
