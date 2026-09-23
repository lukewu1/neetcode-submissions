class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_length = 0
        seen = collections.defaultdict(int)
        for r in range(len(s)):
            seen[s[r]] += 1
            while (r-l+1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            max_length = max(max_length, (r-l+1))
        return max_length
