def play():
    row1 = ['','','']
    row2 = ['','','']
    row3 = ['','','']

    print(row1)
    print(row2)
    print(row3)

play()

def user_choice():
    choice = 'WRONG'

    while choice.isdigit() == False  : 
        choice = input('Enter the value (0-10): ')
        if choice.isdigit() == False:
            print('Sorry that is not a digit')
    
    return int(choice)
choice = user_choice()
print(f'your choice {choice}')