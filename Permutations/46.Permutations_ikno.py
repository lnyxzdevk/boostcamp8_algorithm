class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        result=[]
        useli=[False]*len(nums)
        def perm(nums,useli,length,subset):
            if length==len(nums):
                result.append(subset[:])
                return 
            for i,num in enumerate(nums):
                if useli[i]==False:
                    useli[i]=True
                    subset.append(num)
                    length+=1
                    perm(nums,useli,length,subset)
                    useli[i]=False
                    length-=1
                    subset.pop()
                elif useli[i]==True:
                    continue
        perm(nums,useli,0,subset)
        return result