class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k, total_diff = k1 + k2, sum(diffs)
        if k >= total_diff: return 0
        max_diff = max(diffs)
        counts = [0] * (max_diff + 1)
        for d in diffs: counts[d] += 1
        for i in range(max_diff, 0, -1):
            if counts[i] == 0: continue
            reduce_amount = min(counts[i], k)
            counts[i] -= reduce_amount
            counts[i - 1] += reduce_amount
            k -= reduce_amount
            if k == 0: break
                
        return sum(counts[i] * (i * i) for i in range(max_diff + 1) if counts[i] > 0)