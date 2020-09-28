def f(n: list, m: list) -> (int, int):
    a, b = 0, 0
    for i in range(0, len(n)):
        a = a + i
    for j in range(0, len(m)):
        b = b + j * 2
    return a, b



if __name__ == '__main__':
    # Vos tests ici
    pass
