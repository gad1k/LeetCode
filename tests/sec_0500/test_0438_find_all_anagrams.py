from unittest import TestCase, main
from tasks.sec_0500.task_0438_find_all_anagrams import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.findAnagrams("cbaebabacd", "abc")
        self.assertListEqual([0, 6], r)

    def test02(self):
        r = self.s.findAnagrams("abab", "ab")
        self.assertListEqual([0, 1, 2], r)


if __name__ == '__main__':
    main()
