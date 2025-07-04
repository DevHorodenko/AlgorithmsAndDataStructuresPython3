matrix = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

print(matrix[1][2]) # First element is line, second is column

vector = [
    10,
    20,
    30,
    40,
    50
]

print(vector[-1])

matrixExample = [
    ['Leo', 8, 7, 6],
    ['Peter', 4.5, 9, 10],
    ['Jhon', 6, 6, 8]
]

for line in matrixExample:
    for col in line:
        print(str(col) + '\t', end = ' ')
    print(' ')