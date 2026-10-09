class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open_needed = 0  # Tracks how many ')' pairs we need for our open '('
        
        for char in s:
            if char == '(':
                # Since each '(' needs two ')', if we have an odd number of needed ')',
                # it means the previous '(' only got one ')'. We must insert one ')' right now.
                if open_needed % 2 == 1:
                    ans += 1
                    open_needed -= 1
                open_needed += 2
            else:
                # We encountered a ')'. We decrement our required ')' count.
                open_needed -= 1
                # If open_needed drops below 0, it means we have a ')' without a matching '('.
                # We must insert a '(' (which supplies 2 closing slots), so we add 1 to ans and 2 to open_needed.
                if open_needed < 0:
                    ans += 1
                    open_needed += 2
                    
        return ans + open_needed