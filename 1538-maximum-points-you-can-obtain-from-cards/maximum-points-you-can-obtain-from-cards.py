class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if(k==n):
            return sum(cardPoints)
        ts = sum(cardPoints)
        windowsize=n-k
        win_sum=sum(cardPoints[:windowsize])
        min_w_sum=win_sum
        for i in range(windowsize,n):
            win_sum+=cardPoints[i]-cardPoints[i-windowsize]
            min_w_sum=min(min_w_sum,win_sum)
        return ts-min_w_sum
        