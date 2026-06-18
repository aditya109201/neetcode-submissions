class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [1]

        for i in nums:
            if len(res) == len(nums):
                break
            
            product = product * i
            res.append(product)

        product = 1
        count = len(nums) - 1

        while count > 0:
            product = product * nums[count]
            res[count - 1] = res[count - 1] * product

            count = count - 1

        return res
