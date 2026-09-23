class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        if target < 0: 
            return -1
        if target == 0: 
            return len(nums)

        left = 0
        current_sum = 0
        max_len = -1
        n = len(nums)
        for right in range(n):
            current_sum += nums[right]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                window_len = right - left + 1
                if window_len > max_len:
                    max_len = window_len
                    
        return -1 if max_len == -1 else n - max_len
