class Solution(object):
    def reverseBits(self, n):
        res =""
        while (n != 0):
            rem = n % 2
            if rem == 1:
                res+="1"
            else:
                res+="0"
            n = n//2
        res = res + "0" * (32 - len(res))
        
        dn = 0
        p = 0
        for i in range(len(res)-1,-1,-1):
            if res[i] == "1":
                dn += 2**p
            p += 1
        return dn
        
        