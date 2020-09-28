class Matrix:

    def __init__(self):
        self.matrix = [
            [
                "{}{}".format(j, i) for i in range(0, 10)
            ] for j in range(0, 10)
        ]

    def get(self, i, j):
        if i >= len(self.matrix) or j >= len(self.matrix[0]):
            raise ValueError("Indices out of bound")
        return self.matrix[i][j]


if __name__ == '__main__':
    matrix = Matrix()
    print(matrix.get(9, 9))
