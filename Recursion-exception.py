#recursion & exception
#factorial !number
print('recursion breakdown')
print('1 * 2 = 2 * 3 = 6 * 4 = 24 * 5 = 120 * 6 = 720')
def factorial_1(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial
print(factorial_1(6))
#generators
def get_number():
    for i in range(1, 4):
        yield i
generator = get_number()
print(next(generator), (next(generator)))
print(next(generator))
for x in get_number():
    print(x)
numbers = list(get_number())
print(numbers)
#Exception
while True:
    try:
        num = int(input('provide number '))
        print('value of:', num, 'is', 2/num)
        break
    except ValueError:
        print('You did not enter a number, I will try again')
    except ZeroDivisionError:
        print('please do not divide by 0')
    except:
        print('Sorry something went wrong!')
#exception hierarchy
import sys
name = input('provide your name: ')
if name == '':
    print('Your name is empty, I am going to shut down now')
    sys.exit()
print('Hey there,', name, 'nice to meet you')
#exception propaganda
def months(info):
    month = int(input('What month were you born (1-12): '))
    info.append(month)
def days(info):
    day = int(input('Day you were born (1-31): '))
    info.append(day)
def years(info):
    year = int(input('Provide your birth year: '))
    info.append(year)
    
def bday(info):#the question will presented in order of the try:
    try:
        months(info)
        days(info)
        years(info)
        print('The users birthday: ', info)
    except:
        print('You provided an incorrect value')
    
print('I am collecting data about you!')
info = []
bday(info)
