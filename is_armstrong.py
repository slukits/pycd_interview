from typing import Generator


def test(i: int) -> bool:
    k, exp, got = len(str(i)), i, 0
    while i != 0:
        got += (i % 10) ** k
        if got > exp:
            return False
        i = i // 10
    return got == exp


def gen() -> Generator[int, None, None]:
    a = 0
    while True:
        a += 1
        if test(a):
            yield a
