class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1]*n
        """for i in range(n):
            for j in range(1,n):
                nxt = (i+j)%n
                if nums[i]<nums[nxt]:
                    ans[i] = nums[nxt]
                    break
        return ans"""
        st =[]
        for i in range(2*n):
            idx = i % n
            while st and nums[idx] > nums[st[-1]]:
                prev = st.pop()
                ans[prev] = nums[idx]
            if i < n:
                st.append(idx)
        return ans
            


        