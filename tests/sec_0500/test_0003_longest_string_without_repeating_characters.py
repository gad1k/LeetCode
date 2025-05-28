from unittest import TestCase, main
from tasks.sec_0500.task_0003_longest_string_without_repeating_characters import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, r)

    def test02(self):
        r = self.s.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, r)

    def test03(self):
        r = self.s.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, r)

    def test04(self):
        r = self.s.lengthOfLongestSubstring("au")
        self.assertEqual(2, r)


if __name__ == '__main__':
    main()
