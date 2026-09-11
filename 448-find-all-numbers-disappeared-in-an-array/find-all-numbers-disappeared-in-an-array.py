class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        set_numbers = set(nums)
        missing_numbers = []
        
        for i in range(1,len(nums)+1):

            if i not in set_numbers:
                missing_numbers.append(i)
        
        return missing_numbers
            
        