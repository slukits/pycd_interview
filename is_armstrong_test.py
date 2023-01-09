from tddflow.testing import run, T
import is_armstrong


class IsArmstrong:

    def if_lower_10(self, t: T):
        for p in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            t.truthy(is_armstrong.test(p))

    def for_some_other_known_cases(self, t: T):
        for n in [153, 370, 371, 407]:
            t.truthy(is_armstrong.test(n), str(n))

    def generated(self, t: T):
        gen, aa = is_armstrong.gen(), []
        for i in range(13):
            aa.append(next(gen))
        t.eq(aa, [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])


if __name__ == '__main__':
    run(IsArmstrong)
