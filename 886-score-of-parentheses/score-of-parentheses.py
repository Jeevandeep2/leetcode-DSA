class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans, deapth = 0,0
        for i,c in enumerate(s):
            if c == '(':
                deapth += 1
            else:
                deapth -= 1
                if s[i-1] == '(':
                    ans += 1 << deapth
        return ans

        