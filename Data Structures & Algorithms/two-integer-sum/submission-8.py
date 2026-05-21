class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i in range (0, len(nums)):
            need = target - nums[i]

            if need in counter:
                return [counter[need], i]

            counter[nums[i]] = i