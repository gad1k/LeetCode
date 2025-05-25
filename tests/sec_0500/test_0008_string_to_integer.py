from unittest import TestCase, main
from tasks.sec_0500.task_0008_string_to_integer import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(42, self.s.myAtoi("42"))

    def test02(self):
        self.assertEqual(-42, self.s.myAtoi("  -42"))

    def test03(self):
        self.assertEqual(1337, self.s.myAtoi("1337c0d3"))

    def test04(self):
        self.assertEqual(0, self.s.myAtoi("0-1"))

    def test05(self):
        self.assertEqual(0, self.s.myAtoi("words and 987"))


if __name__ == '__main__':
    main()
