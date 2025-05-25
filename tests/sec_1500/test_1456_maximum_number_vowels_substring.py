from unittest import TestCase, main
from tasks.sec_1500.task_1456_maximum_number_vowels_substring import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.maxVowels("abciiidef", 3)
        self.assertEqual(3, r)

    def test02(self):
        r = self.s.maxVowels("aeiou", 2)
        self.assertEqual(2, r)

    def test03(self):
        r = self.s.maxVowels("leetcode", 3)
        self.assertEqual(2, r)


if __name__ == '__main__':
    main()
