class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st =[]
        ma = 0
        for i  in range(len(heights)):
            start = i
            h = heights[i]
            while st and st[-1][1] > h:
                idx,height = st.pop()
                ma = max(ma,height*(i-idx))
                start = idx
            st.append((start,h))
        for idx,height in st:
            ma = max(ma,height * (len(heights)-idx))
        return ma

        