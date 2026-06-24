class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        counter = {}
        index = 1

        for i in numbers:
            if i not in counter:
                counter[i] = index
                index += 1
            else:
                index += 1

        for i in counter:
            if target - i in counter:
                return [counter[i], counter[target - i]]