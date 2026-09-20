class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i, ch in enumerate(s, start = 1):
            result += (26 - (ord(ch) - ord("a")))*i
        return result
