from unittest import TestCase, main
from tasks.sec_2500.task_2236_root_equals_sum_of_children import Solution, TreeNode


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertTrue(self.s.checkTree(TreeNode(10, 4, 6)))

    def test02(self):
        self.assertFalse(self.s.checkTree(TreeNode(5, 3, 1)))


if __name__ == '__main__':
    main()
