class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) & 1:
            return False

        if grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        dp = [0] * n

        for i in range(m):
            left = 0

            for j in range(n):

                if i == 0 and j == 0:
                    dp[j] = 2
                    left = 2
                    continue

                x = dp[j] | left

                if grid[i][j] == '(':
                    x <<= 1
                else:
                    x >>= 1

                dp[j] = x
                left = x
        return bool(dp[-1] & 1)