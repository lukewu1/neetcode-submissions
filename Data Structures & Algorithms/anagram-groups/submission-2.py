class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = collections.defaultdict(list)
        for i in range(len(strs)):
            str_sorted = "".join(sorted(strs[i]))
            sorted_strings[str_sorted].append(strs[i])
            
        return list(sorted_strings.values())