print('Hello World')
greeting = 'This is my Python Repository!'
print('My name is Asonti,', greeting)
age = 19
I_am_in_school = True
# We are using the Udemy course to help teach Python
print(0.000000000000000000000004) #scientific notation
print(0o163) #octal numbers
print(0x167) #hexadecimal numbers
print(6 / 2) #basic division
print(7 // 2) #integer division
print(6 % 5) #modulus division how much you have left over. this 5 can go into 6, 1 time with 1 number remaining
#no numbers can be divided by 0
print(2 ** 3) #this is a power operator, this is 2 to the power of 3
print('I am currenlty', age, 'I attened a school called:')
school = 'Level ' + 'Up ' + 'In ' + 'Tech'
print(school)
print('LUIT! ' * 5)
print('Now lets learn about you')
print('What school do you attend?')
school = input()
print(school, 'sounds like a great school!')
user = input('Create a username: ')
email = input('Enter your email: ')
print('Hey', user, 'I will be sending an invite email to your', email, 'email shortly!')
#Now lets try TYPE CASTING
print('Now lets find out how old you wil be in 50 years')
your_age = input('How old are you? ')
future_age = float(your_age)
print('In 50 years you will be', future_age + 50, 'years old. WOW thats old')
#We are going to try another method od Type casting
print('How old would you be if you were half your age? ')
half_age = float(input('How old are you? '))
print('If you were half your age you would be', half_age / 2)
#Next is trying the INT
print('Now lets see how old you would be if you lived until 2300')
year = int(input('What year were you born? '))
print('In 2300, you will be', 2300 - year, 'years old. You would live to see flying cars')
