class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0]*k
        dp = [0]*k
        for num in nums:
            next_dp = [0]*k
            next_dp[num % k] += 1
            for i in range(k):
                if dp[i] > 0:
                    new_i = (i * num) % k
                    next_dp[new_i] += dp[i]
            dp = next_dp
            for r in range(k):
                result[r] += dp[r]
                
        return result
