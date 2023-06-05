#TUPLES are immutables
empty_tuple = ()
one_el_tuple_a = (1,)
three_el_tuple_a = 1, 2, 3
print(three_el_tuple_a)
attributes = ('pretty', 'colorful', 'priceless')
print(attributes)
print(attributes[0])
#TUPLE Operations
print(len(attributes))
print(len(three_el_tuple_a))
for att in attributes:
    print(att)
attributes = ('pretty', 'colorful', 'priceless') + ('unique', 'new age')
print(attributes)
numbs = (3, 5) * 3
print(numbs)
#tuples in list
penny = ('brown', 'copper', .01)
quarter = ('silver', 'big', .25)
dollar = ('green', 'rectangular', 1.0)
money = [penny, quarter, dollar]
print(money)
for description in money:
    print('COLOR:', description[0], 'DISTINCTION:', description[1], 'WORTH:', description[2])
#list in tuples
me = ('Asonti', 'Student', 2004, [3.27, 5.29, 8.31])
me[3].append(11.28)
print(me)

