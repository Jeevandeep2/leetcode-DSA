class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # Count how many numbers have each bit set (only touches set bits)
        cnt = [0] * 30
        for x in nums:
            while x:
                low = x & -x
                cnt[low.bit_length() - 1] += 1
                x ^= low

        # Row i of the "stacked" numbers = bits whose count > i.
        # That row stays the same between distinct counts, so group the rows.
        bits = sorted((c, b) for b, c in enumerate(cnt) if c)
        mask = 0
        for _, b in bits:
            mask |= 1 << b

        total = 0
        prev = 0
        for c, b in bits:
            end = c if c < k else k
            if end > prev:
                total += (end - prev) * mask * mask
                prev = end
                if prev == k:
                    break
            mask ^= 1 << b

        return total % MOD