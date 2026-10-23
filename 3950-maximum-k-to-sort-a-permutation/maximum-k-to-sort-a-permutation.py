class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k=-1
        for i in range(len(nums)):
            if nums[i]!=i:
                k=nums[i] if k==-1 else k&nums[i]
        return max(k,0)
        
