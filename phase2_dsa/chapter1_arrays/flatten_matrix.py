def flatten(matrix):
    new_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_list.append(matrix[i][j])
    return new_list

matrix = [
    [12, 56, 86],
    [12, 74, 96],
    [47, 96, 3],
    [5, 6, 2]
]
print(flatten(matrix))