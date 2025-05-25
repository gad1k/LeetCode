from unittest import TestCase, main
from tasks.sec_2500.task_2235_add_two_intergers import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(17, self.s.sum(12, 5))

    def test02(self):
        self.assertEqual(-6, self.s.sum(-10, 4))


if __name__ == '__main__':
    main()
