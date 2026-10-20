class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        if not nums:
            return 0

        N = len(nums)
        
        divisors = []
        for i in range(1, int(math.sqrt(N))+1):
            if N%i == 0:
                divisors.append(i)
                if N//i != i:
                    divisors.append(N//i)
        
        
        answer = 0
        for d in divisors:
            r = 0
            l = 0
            valid = True

            prev_max = float("-inf")
            while r < len(nums):
                start = r
                r += d

                drops = 0
                curr_max = float("-inf")
                curr_min = float("inf")
                
                while l < r:
                    if l+1 < r and nums[l] > nums[l+1]:
                        if drops < 1 and nums[start] >= nums[r-1]:
                            drops+=1
                        else:
                            valid = False
                            break
                    curr_min = min(curr_min, nums[l])
                    curr_max = max(curr_max, nums[l])
                    l+=1
                if not valid:
                    break

                if curr_min < prev_max:
                    valid = False
                    break

                prev_max = curr_max

            if valid:
                answer += d

        return answer