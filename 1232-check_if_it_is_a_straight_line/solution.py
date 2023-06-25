class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        x1 = coordinates[1][0]
        y0 = coordinates[0][1]
        y1 = coordinates[1][1]
        for i, j in coordinates:
            if (x1 - x0) * (j - y1) != (i - x1) * (y1 - y0):
                return False
        return True

# Runtime: 76 ms (beats 71.3%)
# Memory: 16.9 MB (beats 60.29%)
