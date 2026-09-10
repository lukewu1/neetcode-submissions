class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = collections.defaultdict(list)
        for i in range(len(strs)):
            str_sorted = "".join(sorted(strs[i]))
            sorted_strings[str_sorted].append(strs[i])

        output = []
        for i in sorted_strings.keys():
            output.append(sorted_strings[i])
        
        return output