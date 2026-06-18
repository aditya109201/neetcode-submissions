class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prev = product
        zerocount = 0
        for i in nums:
            prev = product
            product = product * i
            if product == 0:
                product = prev
                zerocount += 1

        res = []

        if zerocount >= 2:
            return [0] * len(nums)

        elif zerocount == 1:
            for j in nums:
                if j == 0:
                    res.append(product)
                else:
                    res.append(0)

        else:
            for j in nums:
                res.append(int(product / j))

        return res