class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for i in nums:
            xor = xor^i
        return xor
        