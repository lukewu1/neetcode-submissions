class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_length = 0
        seen = collections.defaultdict(int)
        for r in range(len(s)):
            seen[s[r]] += 1
            if (r-l+1) - max(seen.values()) <= k:
                max_length = max(max_length, (r-l+1))
            else:
                seen[s[l]] -= 1
                l += 1
        return max_length
