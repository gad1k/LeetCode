class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = list()

        for i in range(1, n + 1):
            curVal = ""

            if i % 3 == 0:
                curVal += "Fizz"
            if i % 5 == 0:
                curVal += "Buzz"
            if not curVal:
                curVal = str(i)

            result.append(curVal)

        return result
