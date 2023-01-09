from tddflow.testing import run, T
import reverse_integer


class TheReverse:

    def of_zero_is_zero(self, t: T):
        t.eq(0, reverse_integer.v_str(0))
        t.eq(0, reverse_integer.v_mod(0))

    def of_nm_is_mn(self, t: T):
        t.eq(24, reverse_integer.v_str(42))
        t.eq(24, reverse_integer.v_mod(42))

    def of_nmo_is_onm(self, t: T):
        t.eq(801, reverse_integer.v_str(108))
        t.eq(801, reverse_integer.v_mod(108))


if __name__ == '__main__':
    run(TheReverse)
