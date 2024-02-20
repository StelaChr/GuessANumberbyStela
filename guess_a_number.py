from random import randint

computer_number = randint(1, 100)

while True:
    player_input = input ("Guess the number in range (1- 100): ")
    if not player_input.isdigit() or int(player_input)<1 or int(player_input)>100:
        print ("Invalid input. It should be a number in range (1- 100). Please try again.")
        continue
    if int(player_input) == computer_number:
        print ("Correct! You guessed the number!")
    elif int(player_input) > computer_number:
        print ("Wrong! Too high number.")
    else:
        print ("Wrong! Too low number.")






