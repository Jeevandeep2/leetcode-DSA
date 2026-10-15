class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            seen = [False] * 101
            distinct = 0
            for j in range(i, n):
                if not seen[nums[j]]:
                    seen[nums[j]] = True
                    distinct += 1
                ans += distinct * distinct
        return ans