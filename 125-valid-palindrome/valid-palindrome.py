class Solution(object):
    def isPalindrome(self, s):
        st = ''
        s = s.lower()
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
                st+=i
        return st == st[::-1]
        