class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False

        if grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        dp = [0] * n
        dp[0] = 2

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                x = dp[j]

                if j:
                    x |= dp[j - 1]

                if grid[i][j] == '(':
                    x <<= 1
                else:
                    x >>= 1

                remaining = m + n - i - j - 2
                dp[j] = x & ((1 << (remaining + 1)) - 1)
                
        return bool(dp[-1] & 1)