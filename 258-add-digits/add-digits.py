class Solution(object):
    def addDigits(self, num):
        while num > 9 :
            t = 0
            while num > 0:
                t += num%10
                num = num//10
            num = t
        return(num)
        if num==0:
            return 0
        return 1+(num-1)%9
        """
        :type num: int
        :rtype: int
        """
        