class Matrix():
    def __init__(self, mas):
        self.mas = mas

    def __str__(self):
        a = ""
        for i in self.mas:
            a += f'{" ".join(map(str, i))}\n'
        return f"Ваша матрица:\n{a}"

    def __add__(self, other):
        sum = []
        for i in range(len(self.mas)):
            sum.append([])
            for j in range(len(self.mas[i])):
                sum[i].append(self.mas[i][j] + other.mas[i][j])
        return Matrix(sum)


mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = Matrix(mas)
mas_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m_1 = Matrix(mas_1)
print(m + m_1)
