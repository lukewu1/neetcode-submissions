import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        
        maxHeap = []
        for i in frequency.keys():
            maxHeap.append([-(frequency[i]), i])

        heapq.heapify(maxHeap)

        output = []
        for i in range(k):
            _, num = heapq.heappop(maxHeap)
            output.append(num)
        return output
