def f(n: list) -> int:
    a: int = 0
    i: int = len(n)
    while i > 0:
        a += 1
        i /= 2
    return a


if __name__ == '__main__':
    # Vos tests ici
    pass
