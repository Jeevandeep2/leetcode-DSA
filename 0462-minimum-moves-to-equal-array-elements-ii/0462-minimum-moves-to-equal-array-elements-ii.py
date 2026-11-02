import numpy as np
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        part = np.partition(arr:= np.array(nums), m:=len(nums)//2)
        return int(np.abs(arr-part[m]).sum())