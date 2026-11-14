class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        val = [0] * n
        cnt = [0] * n
        head, tail = 0, -1
        j = n - 1
        cost = 0
        ans = 0

        for i in range(n - 1, -1, -1):
            c = 1
            while tail >= head and val[tail] < nums[i]:
                cost += (nums[i] - val[tail]) * cnt[tail]
                c += cnt[tail]
                tail -= 1
            tail += 1
            val[tail] = nums[i]
            cnt[tail] = c

            while cost > k:
                cost -= val[head] - nums[j]
                cnt[head] -= 1
                if cnt[head] == 0:
                    head += 1
                j -= 1

            ans += j - i + 1
        return ans