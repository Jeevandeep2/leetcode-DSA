
import heapq

class Solution:
    def assignTasks(self, servers, tasks):

        m = len(servers)
        n = len(tasks)

        # Busy: (finishTime, index, weight)
        busy = []

        # Free: (weight, index)
        free = []

        for i in range(m):
            heapq.heappush(free, (servers[i], i))

        ans = [0] * n
        time = 0

        for i in range(n):

            time = max(i, time)

            if not free:
                time = max(time, busy[0][0])

            # Move completed servers to free heap
            while busy and busy[0][0] <= time:
                finishTime, index, weight = heapq.heappop(busy)

                heapq.heappush(free, (weight, index))

            # Pick best available server
            weight, index = heapq.heappop(free)

            ans[i] = index

            # Mark server as busy
            heapq.heappush(
                busy,
                (time + tasks[i], index, weight)
            )

        return ans
        