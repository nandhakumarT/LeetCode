class Solution:
    def countAndSay(self, n: int) -> str:
        """
        def say():
            res=""
            count=1
            n=len(s)
            for i in range (n):
                if i+1<n and n[i]==n[i+1]:
                    count+=1
                    i+=1
                else:
                    res.append(str(count))
                    res.append((n[i]))
                    count+=1
            return ''.join(res)
        
        if n==1:
            return '1'
        else:
            s=self.countAndSay(n-1)
            return say()
        """
        
        def say():
            m = len(s)
            ct = 1
            ans = []
            
            for i in range(m):
                if i + 1 < m and s[i] == s[i+1]:
                    ct += 1
                else:
                    ans.append(str(ct))
                    ans.append(s[i])
                    ct = 1 # reset count
            return ''.join(ans)
        
        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n-1)
            return say()