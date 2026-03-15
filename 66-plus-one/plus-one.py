class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        res=[0]*(n+1)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        res[0]=1
        for j in range(1,n):
            res[j]=0
        return res