class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_remain = [[0] * k for _ in range(4 * n)]
        
        for i in range(n):
            nums[i] %= k
        def merge(left_idx: int, right_idx: int, target_idx: int):
            l_prod = tree_prod[left_idx]
            r_prod = tree_prod[right_idx]
            tree_prod[target_idx] = (l_prod * r_prod) % k
            
            l_rem = tree_remain[left_idx]
            r_rem = tree_remain[right_idx]
            t_rem = tree_remain[target_idx]
            for i in range(k):
                t_rem[i] = l_rem[i]
                
            for j in range(k):
                r_val = r_rem[j]
                if r_val > 0:
                    t_rem[(l_prod * j) % k] += r_val

        # Segment Tree Construction
        def build(cur: int, left: int, right: int):
            if left == right:
                tree_remain[cur][nums[left]] = 1
                tree_prod[cur] = nums[left]
                return
            mid = (left + right) // 2
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2
            build(left_child, left, mid)
            build(right_child, mid + 1, right)
            merge(left_child, right_child, cur)

        # Segment Tree Point Updates
        def update(cur: int, tl: int, tr: int, idx: int, val: int):
            if tl == tr:
                for i in range(k):
                    tree_remain[cur][i] = 0
                tree_remain[cur][val] = 1
                tree_prod[cur] = val
                return
            mid = (tl + tr) // 2
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2
            if idx <= mid:
                update(left_child, tl, mid, idx, val)
            else:
                update(right_child, mid + 1, tr, idx, val)
            merge(left_child, right_child, cur)

        # Temporary containers to avoid dynamic memory initialization during queries
        q_prod = [1]
        q_remain = [0] * k

        # Segment Tree Range Queries
        def query(cur: int, tl: int, tr: int, l: int, r: int, is_first: bool) -> bool:
            
            if l <= tl and tr <= r:
                if is_first:
                    q_prod[0] = tree_prod[cur]
                    for i in range(k):
                        q_remain[i] = tree_remain[cur][i]
                    return False
                else:
                    curr_prod = q_prod[0]
                    next_remain = [0] * k
                    for i in range(k):
                        next_remain[i] = q_remain[i]
                    for j in range(k):
                        r_val = tree_remain[cur][j]
                        if r_val > 0:
                            next_remain[(curr_prod * j) % k] += r_val
                    q_prod[0] = (curr_prod * tree_prod[cur]) % k
                    for i in range(k):
                        q_remain[i] = next_remain[i]
                    return False

            mid = (tl + tr) // 2
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2
            
            if l <= mid:
                is_first = query(left_child, tl, mid, l, r, is_first)
            if r > mid:
                is_first = query(right_child, mid + 1, tr, l, r, is_first)
            return is_first

        build(0, 0, n - 1)
        ans = []
        
        for idx, val, start, xi in queries:
            val %= k
            update(0, 0, n - 1, idx, val)
            query(0, 0, n - 1, start, n - 1, True)
            ans.append(q_remain[xi])
            
        return ans
