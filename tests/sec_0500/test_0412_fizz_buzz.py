from unittest import TestCase, main
from tasks.sec_0500.task_0412_fizz_buzz import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertListEqual(self.s.fizzBuzz(3), ["1", "2", "Fizz"])

    def test02(self):
        self.assertListEqual(self.s.fizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test03(self):
        self.assertListEqual(self.s.fizzBuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                                                   "11", "Fizz", "13", "14", "FizzBuzz"])


if __name__ == '__main__':
    main()