from Board import Board

mastermind = Board(0)

mastermind.generate()

mastermind.schow_bord()

print("----- make guess 1")
guess = []
print("guess 0:")
guess.append(int(input()))
print("guess 1:")
guess.append(int(input()))
print("guess 2:")
guess.append(int(input()))
print("guess 3:")
guess.append(int(input()))
mastermind.make_guess(guess)
mastermind.schow_bord()
print("guess :" + str(mastermind.give_row(0)) + "evaluation :" + str(mastermind.give_evaluation(0)))
print(mastermind.give_row(1) + mastermind.give_evaluation(1))


print("I'm done!")
