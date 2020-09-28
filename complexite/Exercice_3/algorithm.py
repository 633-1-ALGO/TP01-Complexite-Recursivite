def f(n: list) -> int:
    a: int = 0
    i: int = int(len(n) / 2)
    while i <= len(n):
        j: int = 2
        while j <= len(n):
            a += 1
            j *= 2
        i += 1
    return a


if __name__ == '__main__':
    # Vos tests ici
    pass
