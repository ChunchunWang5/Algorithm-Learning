# https://leetcode.cn/problems/is-subsequence/
# 392. 判断子序列

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n>m: return False
        l, r = 0, 0
        while l<n and r<m:
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == n