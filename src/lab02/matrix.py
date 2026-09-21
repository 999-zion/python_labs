def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []: return []
    stroka = len(mat)
    stolb = len(mat[0])
    for i in mat:
        if len(i) != stolb:
            raise ValueError("рваная матрица")
    new = [[0 for i in range(stroka)] for j in range(stolb)]
    for i in range(stroka):
        for j in range(stolb):
            new[j][i] = mat[i][j]
    return new

'''
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
'''

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if (mat == []) or (mat == [[]]):
        raise ValueError("Пустая матрица")
    stolb = len(mat[0])
    for i in mat:
        if len(i) != stolb:
            raise ValueError("рваная")
    sums = []
    for i in mat:
        sums.append(sum(i))
    return sums

'''
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
'''

def col_sums(mat: list[list[float | int]]) -> list[float]:
    stolb = len(mat[0])
    for i in mat:
        if len(i) != stolb:
            raise ValueError("рваная")
    ans = row_sums(transpose(mat))
    return ans

'''
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
'''

