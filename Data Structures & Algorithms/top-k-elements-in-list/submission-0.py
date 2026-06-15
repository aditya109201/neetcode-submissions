class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []

        for num in nums:
            if num in counter:
                counter[num] += 1

            else:
                counter[num] = 1

        sorted_items = sorted(
            counter.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for i in range(k):
            res.append(sorted_items[i][0])

        return res

        