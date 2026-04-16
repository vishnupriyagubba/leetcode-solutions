class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        parent={}
        level=set([beginWord])
        found= False
        while level and not found:
            nl=set()
            for word in level:
                if word in wordset:
                    wordset.remove(word)
            for word in level:
                for i in range(len(word)):
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        nw=word[:i]+ch+word[i+1:]
                        if nw in wordset:
                            if nw not in parent:
                                parent[nw]=[]
                            parent[nw].append(word)
                            nl.add(nw)
                            if nw==endWord:
                                found=True
            level=nl
        res=[]
        def dfs(word,path):
            if word == beginWord:
                res.append(path[::-1])
                return
            if word not in parent:
                return
            for p in parent[word]:
                dfs(p,path+[p])
        if found:
            dfs(endWord,[endWord])
        return res


            

        
        