class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            sortedString = "".join(sorted(s))
            groups[sortedString].append(s)
        
        return list(groups.values())