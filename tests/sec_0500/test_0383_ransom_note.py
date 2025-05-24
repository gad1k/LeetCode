from unittest import TestCase, main
from tasks.sec_0500.task_0383_ransom_note import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertFalse(self.s.canConstruct("a", "b"))

    def test02(self):
        self.assertFalse(self.s.canConstruct("aa", "ab"))

    def test03(self):
        self.assertTrue(self.s.canConstruct("aa", "aab"))


if __name__ == '__main__':
    main()
