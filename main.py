def twoSum(nums, target) -> List[int]:
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            if(sum==target):
                return [i,j]
