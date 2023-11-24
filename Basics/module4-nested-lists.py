numbers = [1, 2, 3, 4]
countries = ['UK', 'US', 'Germany']
countries = [1, 'UK', 2, 'US']

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])
print(cells[0][0])
print(cells[0][1])

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:',x)

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)

table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in cells:
    for cell in row:
        print(cell, '', end='')
    print()

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)