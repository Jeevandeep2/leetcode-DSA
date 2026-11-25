class Solution(object):
    def smallestUniqueSubarray(self, nums):
        MOD = 10**9 + 7
        BASE = 13

        def compute_hash(v, i, j):
            p = 1
            ret = 0
            for idx in range(i, j + 1):
                ret = (ret + v[idx] * p) % MOD
                p = (p * BASE) % MOD
            return ret

        def check(m):
            mp = Counter()
            x = compute_hash(nums, 0, m - 1)
            p = pow(BASE, m - 1, MOD)
            inv = pow(BASE, MOD - 2, MOD)
            mp[x] += 1

            for i in range(len(nums) - m):
                j = i + m
                x = (x - nums[i]) % MOD
                x = (x * inv) % MOD
                x = (x + nums[j] * p) % MOD
                mp[x] += 1

            return any(count == 1 for count in mp.values())

        low, high = 1, len(nums)
        ans = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans