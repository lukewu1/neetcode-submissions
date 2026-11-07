class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for c in count:
            buckets[count[c]].append(c)
        
        res = []
        countOfResults = 0
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                countOfResults += 1
                if countOfResults == k:
                    return res

