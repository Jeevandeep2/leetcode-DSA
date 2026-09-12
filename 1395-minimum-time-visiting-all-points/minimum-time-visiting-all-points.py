class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(1, len(points)):
            result += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
        return result
        
        # result = 0
        # x1, y1 = points.pop()
        # while points:
        #     x2, y2 = points.pop()
        #     result += max(abs(y2-y1), abs(x2-x1))
        #     x2, y2 = x1, y1
        # return result