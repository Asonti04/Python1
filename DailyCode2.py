#Second half of the modules
#if statements
birth = int(input('What year were you born? '))
if birth > 2005:
    print('You must be 18 years or older to view this site.')
elif birth == 2005:
    print('You are now old enough to view this site.')
if birth < 2005:
    print('You are older than 18 years you are able to view this site.')
number = int(input('Pick a number greater than 100 '))
if number < 100:
    print('The number is too small')
else:
    print('Thats how many eggs my chickens lay a month')
# Trying different Operators
guess = int(input('Guess the secret number, win a prize, Warning you only get 1 try: '))
if guess != 6:
    print('Sorry, that was the incorrect number. You lose')
else:
    print('WOW, that must be beginners luck. Your prize is the satisfaction of winning. Hope you love it!')
#BOOLEAN OPS, you can also us OR. If you use all 3 operators it is in order like: Not, and, Or
live = input('What country do you live in ? ')
if not live == 'United States':
    print('You are not eligible for a consultation')
else:
    print('Okay next question')
    state = input('What state are you in? ')
    if live == 'United States' and state == 'Virginia':
        print('You now qualify for a FREE consultation!')
    else:
        print('You must pay a $50 fee for your consultation.')