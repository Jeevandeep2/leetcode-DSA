class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sm = [0] * (4 * n)
        sq = [0] * (4 * n)
        lz = [0] * (4 * n)

        def apply(node, ln, v):
            sq[node] += 2 * v * sm[node] + v * v * ln
            sm[node] += v * ln
            lz[node] += v

        def update(node, l, r, ql, qr):
            if qr < l or r < ql:
                return
            if ql <= l and r <= qr:
                apply(node, r - l + 1, 1)
                return
            mid = (l + r) // 2
            if lz[node]:
                apply(node * 2, mid - l + 1, lz[node])
                apply(node * 2 + 1, r - mid, lz[node])
                lz[node] = 0
            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)
            sm[node] = sm[node * 2] + sm[node * 2 + 1]
            sq[node] = sq[node * 2] + sq[node * 2 + 1]

        last = {}
        ans = 0
        for j, x in enumerate(nums):
            update(1, 0, n - 1, last.get(x, -1) + 1, j)
            last[x] = j
            ans = (ans + sq[1]) % MOD

        return ans