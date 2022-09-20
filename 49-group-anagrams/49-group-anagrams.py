class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs is None:
            return [""]
        if len(strs)==1:
            return [strs]
        res=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            res[key]+=[word]
        return res.values()
        """   
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c) - ord("a")]+=1
            res[tuple(count)].append(s)
        return res.values()
        """        