#Section5
colors = ['pink', 'purple', 'blue', 'red', 'green']
print(colors[3])
print(colors[-3])
print(colors[2:5])
print(colors[:2])
#deleting list elemets
grocery = ['peas', 'milk', 'eggs', 'noodles', 'apples', 'icecream']
print(grocery)
del grocery[2:]
print(grocery)
#adding list elements
grocery.append('cereal')
print(grocery)
grocery.insert(1, 'juice')
print(grocery)
#Iterating List
food_cost = [3.11, 4.33, 6.99, 2.47, 6.25, 4.19]
sum = 0.0
for cost in food_cost:
    sum += cost
print('TOTAL: ', sum)
#changing list position
food_cost[1], food_cost[5] = food_cost[5], food_cost[1]
print(food_cost)
#alphabetize
grocery.sort()
print(grocery)
#ordering numbers & reverse nums
food_cost.sort()
print(food_cost)
food_cost.sort(reverse=True)
print(food_cost)
#sorted is used for temporary 
print(sorted(grocery))
#checking presence
item = input('What item do you need to remove from the list ')
if item in grocery:
    print('Okay! removing', item, 'off the list')
else:
    print('That item is not on the list')
col = input('pick a color ')
if col not in colors:
    print('invaild color')
else:
    print(col, 'is a great choice!')
#copy list
list1 = [7, 8, 9, 10]
list2 = list1[:]
print('List 1', list1, '\nList 2', list2)
list3 = list1[:2]
print(list3)
numbas1 = []
for i in range(1, 35):
    numbas1.append(i)
print(numbas1)
#using loop for list
numbas = [i for i in range(1, 25)]
print(numbas)
print(list1[:3])
print(list1[3:])
