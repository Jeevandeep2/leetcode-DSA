class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sq = sorted(x * x for x in nums)
        return sum(sq) - 2 * sum(sq[:len(sq) // 2])  # add everything, then flip the smallest half to minus