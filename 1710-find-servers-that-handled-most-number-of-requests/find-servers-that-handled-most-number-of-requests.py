class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        # min heap
        available = list(range(k))
        # busy heap
        busy=[]
        res = [0] * k
        for i, a in enumerate(arrival):
            # these are done, put them back as available
            while busy and busy[0][0] <= a:
                _, x = heapq.heappop(busy)
                # min(available) is at least i, at most i+k-1
                heapq.heappush(available, i + (x-i)%k)
            if available:
                j = heapq.heappop(available) % k
                heapq.heappush(busy, (a+load[i], j))
                res[j] += 1
                
        a= max(res)
        return [i for i in range(k) if res[i] == a]

        