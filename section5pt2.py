#nestedlist/ multi dimensional
grid = [['1a', '1b', '1c'], ['a1', 'b1', 'c1'], ['aa1', 'aa2', 'aa3' ]]
print(grid[2][2])
for x in grid:
    print('value:', x)
print('different way')
for x in grid:
    for y in x:
        print('Values:', y)
print('ANOTHER WAY')
#lets print like a grid
print('PRINT LIKE A GRID')
for row in grid:
    for cell in row:
        print(cell, ' ', end= ' ')
    print()
table = [[i for i in range(1,11)] for k in range(6)]
print(table)
for cube in table:
    for num in cube:
        print(num,' ', end= ' ')
    print()
#add lists
nums = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 9]
numbs3 = nums + nums2
print(numbs3)
#multiply list
numbers = [2, 4, 6, 8] * 5
print(numbers)
name = 'asonti'
print(name[4])
print(name[:3])
print(name[3:])
#capitalization
name_cap = name.upper()
print(name_cap)
