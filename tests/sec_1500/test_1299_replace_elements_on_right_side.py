from unittest import TestCase, main
from tasks.sec_1500.task_1299_replace_elements_on_right_side import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [17, 18, 5, 4, 6, 1]
        self.assertListEqual(self.s.replaceElements(nums), [18, 6, 6, 6, 1, -1])

    def test02(self):
        nums = [400]
        self.assertListEqual(self.s.replaceElements(nums), [-1])


if __name__ == '__main__':
    main()
