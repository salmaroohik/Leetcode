class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        maxi=float('inf')
        summ=0
        nums.sort()
        for i in range(len(nums)):
            hi,lo=len(nums)-1,i+1
            while lo<hi:
                summ=nums[i]+nums[lo]+nums[hi]
                if (abs(target-summ))<abs(maxi):
                    maxi=target-summ
                if summ<target:
                    lo+=1
                else:
                    hi-=1
                if summ==target:
                    break
        return target-maxi
                    
