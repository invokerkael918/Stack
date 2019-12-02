class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, heights):
        # write your code here
        if len(heights) == 0:
            return 0
        stack = []
        area = 0
        for i, height in enumerate(heights + [0]):
            while stack and height <= heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = max(area, width * h)
            stack.append(i)
        return area
