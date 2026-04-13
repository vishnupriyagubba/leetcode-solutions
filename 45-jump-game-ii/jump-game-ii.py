class Solution:
    def jump(self, nums: List[int]) -> int:
        ce=0
        f=0
        j=0
        n=len(nums)
        for i in range(n-1):
            f=max(f,i+nums[i])
            if i==ce:
                j+=1
                ce=f
        return j

        