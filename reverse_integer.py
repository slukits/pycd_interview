def v_str(i: int) -> int:
    return int(''.join(reversed(str(i))))


def v_mod(i: int) -> int:
    inv = 0
    while i != 0:
        inv = inv*10 + i % 10  # add last position of i
        i = i // 10
    return inv