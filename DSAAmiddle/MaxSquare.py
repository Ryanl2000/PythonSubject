#最大正方形
def MaxSquare(arr):  # 常规解法O(N**3 * N)
    m = len(arr)
    n = len(arr[0])
    maxs = float('-inf')
    for row in range(m):
        for col in range(n):
            for board in range(1, min(m-row, n-col)+1):
                flag = 1
                for i in range(row, row + board):
                    if arr[i][col] == 0 or arr[i][col + board - 1] == 0:
                        flag = 0
                        break
                for i in range(col, col + board):
                    if arr[row][i] == 0 or arr[row + board - 1][i] == 0:
                        flag = 0
                        break
                if flag:
                    maxs = max(maxs, board)
    return maxs


def get(arr, i, j):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]):
        return 0
    return arr[i][j]


def MaxSquareUltar(arr):  # 预处理数组解法O(N**3 * 1)
    m = len(arr)
    n = len(arr[0])
    maxs = float('-inf')
    right = [[0 for _ in range(n)] for _ in range(m)]
    down = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m-1, -1, -1):  # 预处理右向和下向数组
        for j in range(n-1, -1, -1):
            if arr[i][j] == 1:
                right[i][j] += (get(right, i, j + 1) + 1)
                down[i][j] += (get(down, i + 1, j) + 1)
            else:
                right[i][j], down[i][j] = 0, 0
    for row in range(m):
        for col in range(n):
            for board in range(1, min(m-row, n-col)+1):
                if 0 < right[row][col] <= board and 0 < down[row][col] <= board:
                    if right[row][col + board - 1] and down[row + board - 1][col]:
                        maxs = max(maxs, board)
    return maxs


arr = [[0, 1, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 1], [0, 1, 0, 1, 1]]
print(MaxSquare(arr))
print(MaxSquareUltar(arr))
