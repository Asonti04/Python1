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
