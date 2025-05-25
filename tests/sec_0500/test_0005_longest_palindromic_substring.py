from unittest import TestCase, main
from tasks.sec_0500.task_0005_longest_palindromic_substring import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.longestPalindrome("babad")
        self.assertEqual("bab", r)

    def test02(self):
        r = self.s.longestPalindrome("cbbd")
        self.assertEqual("bb", r)


if __name__ == '__main__':
    main()
