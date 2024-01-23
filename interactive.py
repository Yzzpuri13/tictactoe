game_list = [0,1,2]

def display_game(game_list):
    print("here is the current list")
    print(game_list)

display_game(game_list )

def position_check():

    choice = 'wrong'

    while choice not in ['0','1', '2']:
        choice = input("Pick a position: ")
        

        if choice not in ['0', '1','2']:
            print('Sorry invalid choice try again!')
            


    return int(choice)

position_check()

def replacement_value(game_list, position):
    user_placement = input('Enter the string at replacement: ')

    game_list[position] = user_placement 

    return game_list

replacement_value(game_list,1)

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep Playing? (Y or N): ")
        

        if choice not in ['Y', 'N']:
            print('Sorry invalid Please choose y or n')
            
    if choice == 'Y':
        return True
    else:
        return False
gameon_choice()

game_list = [0,1,2]

def display_game(game_list):
    print("here is the current list")
    print(game_list)

display_game(game_list )

def position_check():

    choice = 'wrong'

    while choice not in ['0','1', '2']:
        choice = input("Pick a position: ")
        

        if choice not in ['0', '1','2']:
            print('Sorry invalid choice try again!')
            


    return int(choice)

position_check()

def replacement_value(game_list, position):
    user_placement = input('Enter the string at replacement: ')

    game_list[position] = user_placement 

    return game_list

replacement_value(game_list,1)

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep Playing? (Y or N): ")
        

        if choice not in ['Y', 'N']:
            print('Sorry invalid Please choose y or n')
            
    if choice == 'Y':
        return True
    else:
        return False
gameon_choice()

gameon = True
game_list = [0,1,2]

while gameon == True:
    display_game(game_list)

    position = position_check()

    game_list=replacement_value(game_list, position)

    display_game(game_list)

    gameon = gameon_choice()

