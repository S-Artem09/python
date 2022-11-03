matrix = [[1, 5, 3],
          [4, 6, 8],
          [9, 0, 7]]

# print(matrix[2][2])
# print(matrix[0][1])
# print(matrix[2][0])
# print(matrix[2])

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            print(matrix[i][j])