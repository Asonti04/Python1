#Refund Policy Helper
age= int(input('How many days ago have you purchased the item? '))
used= input('Have you used the item at all [y/n]? ')
broke= input('Has the item broken down on its own [y/n]? ')
#policy less 10 days & not used item OR
#policy any day purchase broke on its own
if age <= 10 and used == 'n' or broke == 'y':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')