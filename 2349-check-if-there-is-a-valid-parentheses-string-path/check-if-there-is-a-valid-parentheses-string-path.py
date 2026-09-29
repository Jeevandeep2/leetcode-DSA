class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Path length must be even
        if (m + n - 1) & 1:
            return False

        # Valid parentheses must start with '(' and end with ')'
        if grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        # Bitset DP
        dp = [0] * n

        for i in range(m):
            left = 0

            for j in range(n):

                # Starting cell
                if i == 0 and j == 0:
                    dp[j] = 2
                    left = 2
                    continue

                # Paths can come from top or left
                x = dp[j] | left

                # Current character
                if grid[i][j] == '(':
                    x <<= 1
                else:
                    x >>= 1

                dp[j] = x
                left = x
        return bool(dp[-1] & 1)