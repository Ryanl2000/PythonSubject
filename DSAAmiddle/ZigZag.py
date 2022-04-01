# zigzag问题和旋转正方形问题
def zigzag(arr):
    n = len(arr)
    m = len(arr[0])
    ai, aj, bi, bj = 0, 0, 0, 0
    flag = -1
    while True:
        if flag == 1:
            ki, kj = ai, aj
        else:
            ki, kj = bi, bj
        while True:
            print(arr[ki][kj], end='-')
            if flag == 1 and (ki, kj) == (bi, bj):
                break
            elif flag == -1 and (ki, kj) == (ai, aj):
                break
            ki += flag
            kj -= flag
        flag = - flag
        ai = ai if aj < m - 1 else ai + 1
        aj = aj + 1 if aj < m - 1 else aj
        bj = bj if bi < n - 1 else bj + 1
        bi = bi + 1 if bi < n - 1 else bi
        if ai == n - 1 and bj == m - 1:
            print(arr[-1][-1])
            break


def rotateEdge(arr, x1, y1, x2, y2):  #旋转边
    for i in range(x2-x1):
        arr[x1+i][y2], arr[x2][y2-i], arr[x2-i][y1], arr[x1][y1+i] = \
            arr[x1][y1+i], arr[x1+i][y2], arr[x2][y2-i], arr[x2-i][y1]

    return arr


def rotateSquare(arr):  #旋转矩形
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        rotateEdge(arr, i, i, j, j)
        i += 1
        j -= 1
    return arr


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotateSquare(a))
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zigzag(arr)
