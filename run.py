import os

from Board import Board

def start_mastermind():
    temp_difficulty_select = 0
    ant = " ";
    #setting up the game by selecting a difficulty
    while temp_difficulty_select != 1:
        if temp_difficulty_select == -1:
            print("That was not a valid number")
        print("Difficulty options:")
        print("Easy  :0")
        print("Medium:1")
        print("Select a difficulty setting :")
        ant = input()
        try:
            if (int(ant) == 0) or (int(ant) == 1) :
                mastermind = Board(int(ant))
                mastermind.generate()
                temp_difficulty_select = 1
            else:
                temp_difficulty_select = -1
        except Exception as e:
            temp_difficulty_select = -1
        os.system('cls')
    #running the game
    game_won = mastermind.give_boardstare()
    while  game_won == 0:
        print("Game Difficulty: " + str(mastermind.difficulty) + ", currently at row: "+ str(mastermind.give_current_row()+1))
        print("|   Game guesses:   ||    Evaluations:   |")
        print(" =01= =02= =03= =04=  ==== ==== ==== ==== ")
        for row_count in range(8,-1,-1):
            temp_row = mastermind.give_row(row_count)
            temp_row_evaluation = mastermind.give_evaluation(row_count)
            print( "| " + str(temp_row[0]).zfill(2) + " | "  + str(temp_row[1]).zfill(2) + " | "  + str(temp_row[2]).zfill(2) + " | "  + str(temp_row[3]).zfill(2) + " || "  + str(temp_row_evaluation[0]).zfill(2) + " | "  + str(temp_row_evaluation[1]).zfill(2) + " | "  + str(temp_row_evaluation[2]).zfill(2) + " | "  + str(temp_row_evaluation[3]).zfill(2) + " | ")
        print(" ==== ==== ==== ====  ==== ==== ==== ====")
        guess = []
        print("guess 1:")
        try:
            guess.append(int(input()))
        except Exception as e:
            guess.append(0)
        print("guess 2:")
        try:
            guess.append(int(input()))
        except Exception as e:
            guess.append(0)
        print("guess 3:")
        try:
            guess.append(int(input()))
        except Exception as e:
            guess.append(0)
        print("guess 4:")
        try:
            guess.append(int(input()))
        except Exception as e:
            guess.append(0)
        mastermind.make_guess(guess)
        game_won = mastermind.give_boardstare()
        os.system('cls')
    print("Game Difficulty: " + str(mastermind.difficulty) + ", currently at row: "+ str(mastermind.give_current_row()+1))
    print("| Game guesses:     || Evaluations:      |")
    print(" =01= =02= =03= =04=  ==== ==== ==== ==== ")
    for row_count in range(8,-1,-1):
        temp_row = mastermind.give_row(row_count)
        temp_row_evaluation = mastermind.give_evaluation(row_count)
        print( "| " + str(temp_row[0]).zfill(2) + " | "  + str(temp_row[1]).zfill(2) + " | "  + str(temp_row[2]).zfill(2) + " | "  + str(temp_row[3]).zfill(2) + " || "  + str(temp_row_evaluation[0]).zfill(2) + " | "  + str(temp_row_evaluation[1]).zfill(2) + " | "  + str(temp_row_evaluation[2]).zfill(2) + " | "  + str(temp_row_evaluation[3]).zfill(2) + " | ")
    print(" ==== ==== ==== ====  ==== ==== ==== ====")
    if mastermind.give_boardstare() == 1:
        print("Well done you won!")
        print("In " + str(mastermind.give_current_row()) + " guesses.")
        print("the correct answer was: " + str(mastermind.show_solution()))
    else:
        print("You lost :(")
        print("the correct answer was: " + str(mastermind.show_solution()))
start_mastermind()

print("I'm done!")
