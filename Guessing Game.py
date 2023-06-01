while True:
    guess = int(input('Guess how many countires are in entire world today: '))
    if guess > 196:
        print('No Try Again, Go Lower')
    elif guess < 196:
        print('No Try Again, Go higher')
    else:
        print('''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~CORRECT~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
        break