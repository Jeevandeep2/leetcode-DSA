class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: Calculate the exact minimum number of '(' and ')' to remove
        rem_left = 0
        rem_right = 0
        
        for char in s:
            if char == '(':
                rem_left += 1
            elif char == ')':
                if rem_left > 0:
                    rem_left -= 1
                else:
                    rem_right += 1
        
        result = set()
        
        # Step 2: Backtracking with aggressive pruning
        def dfs(index: int, left_rem: int, right_rem: int, balance: int, path: list[str]):
            # Early pruning: if balance goes negative, the expression is invalid
            if balance < 0:
                return
                
            # Base Case: Reached the end of the string
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    result.add("".join(path))
                return
            
            char = s[index]
            
            if char == '(':
                # Option 1: Remove '(' if we still have a removal budget
                if left_rem > 0:
                    dfs(index + 1, left_rem - 1, right_rem, balance, path)
                
                # Option 2: Keep '('
                path.append(char)
                dfs(index + 1, left_rem, right_rem, balance + 1, path)
                path.pop() # Backtrack
                
            elif char == ')':
                # Option 1: Remove ')' if we still have a removal budget
                if right_rem > 0:
                    dfs(index + 1, left_rem, right_rem - 1, balance, path)
                
                # Option 2: Keep ')'
                path.append(char)
                dfs(index + 1, left_rem, right_rem, balance - 1, path)
                path.pop() # Backtrack
                
            else:
                # Letters must always be kept
                path.append(char)
                dfs(index + 1, left_rem, right_rem, balance, path)
                path.pop() # Backtrack

        # Start the recursive search
        dfs(0, rem_left, rem_right, 0, [])
        return list(result)
