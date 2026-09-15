class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        
        while i < n:
            if i + k <= n and s[i:i+k] == s[i:i+k][::-1]:
                ans += 1
                i += k  
            elif i + k + 1 <= n and s[i:i+k+1] == s[i:i+k+1][::-1]:
                ans += 1
                i += k + 1  
            else:
                i += 1  
                
        return ans