class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start^goal
        res = bin(ans).count("1")
        return res
        