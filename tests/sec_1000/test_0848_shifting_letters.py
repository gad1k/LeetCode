from unittest import TestCase, main
from tasks.sec_1000.task_0848_shifting_letters import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.shiftingLetters("abc", [3, 5, 9])
        self.assertEqual("rpl", r)

    def test02(self):
        r = self.s.shiftingLetters("aaa", [1, 2, 3])
        self.assertEqual("gfd", r)

    def test03(self):
        r = self.s.shiftingLetters("ruu", [26, 9, 17])
        self.assertEqual("rul", r)


if __name__ == '__main__':
    main()
