from unittest import TestCase, main
from tasks.sec_0500.task_0003_longest_string_without_repeating_characters import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        k = self.s.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, k)

    def test02(self):
        k = self.s.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, k)

    def test03(self):
        k = self.s.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, k)

    def test04(self):
        k = self.s.lengthOfLongestSubstring("au")
        self.assertEqual(2, k)


if __name__ == '__main__':
    main()
