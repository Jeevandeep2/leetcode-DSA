class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False

        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = set()

                if i > 0:
                    cur |= dp[j]

                if j > 0:
                    cur |= dp[j - 1]

                if grid[i][j] == '(':
                    dp[j] = {x + 1 for x in cur}
                else:
                    dp[j] = {x - 1 for x in cur if x > 0}

        return 0 in dp[-1]