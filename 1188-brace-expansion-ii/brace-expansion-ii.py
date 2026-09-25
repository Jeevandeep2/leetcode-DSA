class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def combine(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def solve(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':

                if expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    inside, i = solve(i + 1)

                    current = combine(current, inside)

                    i += 1

                else:
                    current = combine(current, {expression[i]})
                    i += 1

            result.update(current)

            return result, i

        result, _ = solve(0)

        return sorted(result)