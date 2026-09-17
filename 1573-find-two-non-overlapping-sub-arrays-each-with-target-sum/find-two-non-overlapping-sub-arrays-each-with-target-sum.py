class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] tracks the shortest valid subarray found in arr[0...i]
        # Using a fixed size array is much faster than map lookups
        min_len = [n + 1] * n  
        
        left = 0
        current_sum = 0
        best_total = n + 1
        best_single = n + 1
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # Valid subarray found
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check for a non-overlapping valid subarray to the left
                if left > 0 and min_len[left - 1] <= n:
                    if curr_len + min_len[left - 1] < best_total:
                        best_total = curr_len + min_len[left - 1]
                
                if curr_len < best_single:
                    best_single = curr_len
            
            min_len[right] = best_single
            
        return best_total if best_total <= n else -1