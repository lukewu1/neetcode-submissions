class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(key = lambda x: x[0])
        time_needed = []
        for pair in pairs:
            time = -(-(target - pair[0])/pair[1])
            while time_needed and time >= time_needed[-1]:
                time_needed.pop()
            time_needed.append(time)
        
        return len(time_needed)