class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        saved = [-1] * n
        size = [1] * n

        stack = [0]
        while stack:
            x = stack.pop()

            if x >= 0:
                c = ord(s[x]) - 97
                saved[x] = last[c]
                last[c] = x
                stack.append(~x)
                stack.extend(children[x])
            else:
                x = ~x
                c = ord(s[x]) - 97
                last[c] = saved[x]
                if x != 0:
                    new_parent = saved[x] if saved[x] != -1 else parent[x]
                    size[new_parent] += size[x]

        return size