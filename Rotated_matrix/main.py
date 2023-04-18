def rotate_matrix(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(length):
        matrix[i] = matrix[i][::-1]
    return matrix

#def main():
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix(matrix))

#if __name__ == "__main__":
   # main()