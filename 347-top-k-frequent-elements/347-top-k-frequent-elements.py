class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        heap={}
        res=[]
        for i in range(len(nums)):
            for i in heap:
                if nums[i]==heap:
                    heap+=1
                elif heap>k:
                    res.append(heap)
                else:
                    continue
        """
        heap={}
        freq=[[] for i in range(len(nums)+1)]
        #creating the frequence table of key as i(count) for lenght of nums plus one times
        # i(count)[0,1,2,3,4,5,6]
        # items   []
        
        for n in nums:
            heap[n]=heap.get(n,0)+1   
        #mapping n with nums and counting the frequence
            
        for n,c in heap.items():
            freq[c].append(n)
        #adding the match freq of values present in the nums
        
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        #for range of length of -1 of freq,till 0th index,by reverse order -1
        #checking the matching value with freq, n which has mapped value from nums 
        #if yes, append to res 
        #if the len(res) is equal to k, where k indicate the how many top freq to return
            
            
            
            
