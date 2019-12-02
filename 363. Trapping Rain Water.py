class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        if not heights:
            return 0

        stack = []
        trapped_water = 0
        for hi_index, height in enumerate(heights):

            while stack and heights[stack[-1]] < height:
                ground_height = heights[stack.pop()]
                if stack:
                    lo_index = stack[-1]
                    water_line = min(heights[lo_index], height)
                    trapped_water += (water_line - ground_height) * (hi_index - lo_index - 1)

            stack.append(hi_index)
        return trapped_water


class SolutionTwoPointer:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        if not heights:
            return 0

        left_max = []
        curt_max = -sys.maxsize
        for height in heights:
            curt_max = max(curt_max, height)
            left_max.append(curt_max)

        right_max = []
        curt_max = -sys.maxsize
        for height in reversed(heights):
            curt_max = max(curt_max, height)
            right_max.append(curt_max)

        right_max = right_max[::-1]

        water = 0
        n = len(heights)
        for i in range(n):
            water += (min(left_max[i], right_max[i]) - heights[i])
        return water