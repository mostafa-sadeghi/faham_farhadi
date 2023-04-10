import random
# for i in range(10):
#     my_number = random.randrange(10000000,12000001)
#     print(my_number)
actions = ["rock", "paper", "scissors"]
res = ''
while res != 'quit':
    player_hand = ''
    computer_hand = random.choice(actions)
    print("enter your choice:")
    print('Rock : 0, Paper: 1, Scissors: 2')
    player_choice = input('> ')
    if player_choice == '0':
        player_hand = 'rock'
    elif player_choice == '1':
        player_hand = 'paper'
    elif player_choice == '2':
        player_hand = 'scissors'

    if player_hand == 'rock' and computer_hand == 'scissors':
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("player wins!")
        print('enter to continue ... or quit to exit')
        res = input('> ')

    elif player_hand == 'paper' and computer_hand == 'rock':
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("player wins!")
        print('enter to continue ... or quit to exit')
        res = input('> ')
    elif player_hand == 'scissors' and computer_hand == 'paper':
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("player wins!")
        print('enter to continue ... or quit to exit')
        res = input('> ')

    elif player_hand == 'scissors' and computer_hand == 'rock':
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("computer wins!")
        print('enter to continue ... or quit to exit')
        res = input('> ')

    elif player_hand == 'rock' and computer_hand == 'paper':
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("computer wins!")
        print('enter to continue ... or quit to exit')
        res = input('> ')
    elif player_hand == 'paper' and computer_hand == 'scissors':
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("computer wins!")
        print('enter to continue ... or quit to exit')
        res = input('> ')
    else:
        print("player's hand", player_hand)
        print("computer's hand:", computer_hand)
        print("equal")
        print('enter to continue ... or quit to exit')
        res = input('> ')
