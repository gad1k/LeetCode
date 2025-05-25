class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        cnt = 0
        if len(flowerbed) == 1:
            possible = self.canPlaceFlower(0, flowerbed[0], 0)
            if possible:
                cnt += 1
            return cnt >= n

        for i in range(len(flowerbed)):
            if i == 0:
                possible = self.canPlaceFlower(0, flowerbed[i], flowerbed[i + 1])
            elif i == len(flowerbed) - 1:
                possible = self.canPlaceFlower(flowerbed[i - 1], flowerbed[i], 0)
            else:
                possible = self.canPlaceFlower(flowerbed[i - 1], flowerbed[i], flowerbed[i + 1])
            if possible:
                flowerbed[i] = 1
                cnt += 1

        return cnt >= n


    def canPlaceFlower(self, left, mid, right):
        return left == 0 and mid == 0 and right == 0
