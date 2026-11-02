class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        minDiff=0
        for i in range(n):
            minDiff+=abs(nums[i]-nums[n//2])
        return minDiff