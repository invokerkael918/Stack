class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """

    def maximalRectangle(self, matrix):
        # write your code here
        if len(matrix) == 0:
            return 0
        max_rectangle = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num else 0
            max_rectangle = max(
                max_rectangle,
                self.largestRectangleArea(heights),
            )

        return max_rectangle

    def largestRectangleArea(self, heights):
        # write your code here
        if len(heights) == 0:
            return 0
        stack = []
        area = 0
        for i, height in enumerate(heights + [0]):

            while (stack and height <= heights[stack[-1]]):
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = max(area, width * h)
            stack.append(i)
        return area