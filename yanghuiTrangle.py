class Triangle:
    def __init__(self, n):
        self.n = n
        print('%d行对应的杨辉三角形如下：'% self.n)
    def setTriangle(self):
        triangle = [[1 for i in range(self.n)]for j in range(self.n)]
        for i in range(2, self.n + 1):
            triangle.append([1]*i)
            for j in range(1, i-1):
                triangle[i-1][j] = triangle[i-2][j] + triangle[i-2][j-1]
        print(triangle[0][0])
        for i in range(1, self.n):
            for j in range(0, i + 1):
                print(triangle[i][j], end = ' ')
            print('')

x = int(input('请输入行数：'))
a = Triangle(x)
a.setTriangle()