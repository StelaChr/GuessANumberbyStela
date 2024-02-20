from random import randint

computer_number = randint(1, 100)
inputs_counter = 0

while True:
    player_input = input (f"You have {10 - inputs_counter} trials to guess the number in range (1- 100): ")
    inputs_counter+=1
    if not player_input.isdigit() or int(player_input)<1 or int(player_input)>100:
        print ("Invalid input. It should be a number in range (1- 100). Please try again.")
        continue
    if int(player_input) == computer_number:
        print ("Correct! You guessed the number!")
    elif int(player_input) > computer_number:
        print ("Wrong! Too high number.")
    else:
        print ("Wrong! Too low number.")
    if inputs_counter== 10:
        print ("Sorry! You lost. No more trials. Do you want to play again (Y/N):")
        player_input2 = input()
        if player_input2 == "Y":
            inputs_counter= 0
        elif player_input2 == "N":
            print ("Thanks for playing!Goodbye!")
            break





