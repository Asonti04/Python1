x= int(input('How many EC2 Instances would you like? '))
dept= input('What department do you work for? ')
import random
list1=['a', 'x', 'y', 'r', 'e', 'b', 'k', 'h']
a=random.randint(0,7)
b=random.randint(0,7)
print('Your randomized Instance Names: ')
for z in range(x):
    print(random.randrange(1,100), dept + list1[a] + list1[b], random.randrange(1,100), sep='_')
