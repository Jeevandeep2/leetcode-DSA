class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        start = 0
        for r in range(k - 1, n):
            for length in range(k, r - start + 2):
                l = r - length + 1
                if l < start:
                    continue
                if self.check(s, l, r):
                    ans += 1
                    start = r + 1
                    break
        return ans

    def check(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True