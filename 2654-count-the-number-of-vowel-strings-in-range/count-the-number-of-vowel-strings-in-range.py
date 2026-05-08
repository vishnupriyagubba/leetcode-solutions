class Solution(object):
    def vowelStrings(self, words, left, right):
        v = ['a','e','i','o','u']
        c = 0
        for i in range(left,right+1):
            word = words[i]
            if word[0] in v and word[-1] in v:
                c+=1
        return c
        