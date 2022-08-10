class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #initalize nums1 and nums2 as a,b 
        a,b=nums1,nums2
        total=len(a)+len(b)
        half=total//2
        
        #checking whether a is smaller than b else make b as a
        if len(b)<len(a):
            a,b=b,a
        
        l,r=0,len(a)-1
        while True:
            i=(l+r)//2 #a
            j=half-i-2#b
            
            aleft=a[i] if i>=0 else float("-infinity")
            aright=a[i+1] if (i+1)<len(a) else float ("infinity")
            bleft=b[j] if j>=0 else float("-infinity")
            bright=b[j+1] if (j+1)<len(b) else float ("infinity")
            
            if aleft<=bright and bleft<=aright:
                #odd
                if total%2:
                    return min(bright,aright)
                #even
                return (max(aleft,bleft)+min(aright,bright))/2
            elif aleft>bright:
                r=i-1
            else:
                l=i+1   
        
        
        
        
        
        
        
        
        
        
       # marray=[]
        
        #if (len(nums1) or len(nums2))==0: return 0
        
       # for i in range(len(nums1)):
        #    marray.append(nums1[i])
        #for j in range(len(nums2)):
         #   marray.append(nums2[j])
            
        #marray.sort()
        #q=len(marray)
        #p=0
        
        #if q/2==0:
         #   p=(q/2)-1
          #  p=(marray[p]+marray[p+1])/2
           # return (p,".5f")
            
       # else:
        #    p=(q-1)/2
         #   p=marray[p]
          #  return (p,".5f")
            
            
            
            
        