class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open_needed = 0 
        for char in s:
            if char == '(':
                if open_needed % 2 == 1:
                    ans += 1
                    open_needed -= 1
                open_needed += 2
            else:
                open_needed -= 1
                if open_needed < 0:
                    ans += 1
                    open_needed += 2
        return ans + open_needed