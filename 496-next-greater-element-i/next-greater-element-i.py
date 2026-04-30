class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st =[]
        nge = {}
        for num in reversed(nums2):
            while st and st[-1] <= num:
                st.pop()
            if st:
                nge[num] = st[-1]
            else:
                nge[num] = -1
            st.append(num)
        res = []
        for i in nums1:
            res.append(nge[i])
        return res

