#Functions
def greet():
    print('HEY THERE!')
greet()
#with parameters
def calc_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    print(average)
calc_average([176.33, 3.1, 77.2, 83.12, 8]) #the list is considered an argument
greet(), calc_average([176.33, 3.1, 77.2, 83.12, 8])
#testing 2 arguments
def letter_count(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count +=1
    print('This sentance contains', count, 'letter', letter)
letter_count('Hello my name is Asonti, I attened the school level up in tech', 'e')
letter_count(text='I never tried biscuits and gravy', letter='i')
#default letter
def letter_count1(text, letter='a'):
    count = 0
    for char in text:
        if char == letter:
            count +=1
    print('This sentance contains', count, 'letter', letter)
letter_count1('apples make apple juice')
#default both
def letter_count3(text='Hello happy people thank you for viewing my code', letter='e'):
    count = 0
    for char in text:
        if char == letter:
            count +=1
    print('This sentance has the letter', letter, ',', count, 'times')
letter_count3()
#Name scopes
def truth():
    variable = 'hey' #local variable
    print(variable)
variable = int(input('guess a number: '))#global variable
print(variable)
truth()
#global namescopes
def kid(): 
    global kidname #assigns this globally
    kidname = 'Jaysun'
    print('welcome in', kidname)
kidname = 'sonti'
print(kidname) #this will print sonti because it is before the kid() is called
kid()
print(kidname) #this prints jaysun because it is after the kid() is called
#none value
x = None #none has no value meaning none
if x is None:
    print('I guess x is none')
if x == None:
    print('YES i guess so!')
random = print('Hey')
print(random)
#return
def calc_average2(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average
print('the average is:', calc_average2([2,88, 3.1, 7.2, 1.5]))
average = calc_average2([2,88, 3.1, 7.2, 1.5])
if average > 10.0:
    print('the average is above normal')