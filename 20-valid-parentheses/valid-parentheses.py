class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """st = []
        for ch in s:
            if ch in '({[':
                st.append(ch)
            else:
                if not st:
                    return False
                top = st.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False
        return not st"""
        #using mapping concept:
        st =[]
        mapi = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in mapi:
                if st:
                    top = st.pop()
                else:
                    top = '#'
                if mapi[ch] != top:
                    return False
            else:
                st.append(ch)
        return not st