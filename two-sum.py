class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n1 = 0
        n2 = 1
        l = len(nums)-1
        while n1 < l:
            total = nums[n1]+nums[n2]
            if total == target:
                return [n1,n2]
            n2 += 1
            if n2 > l:
                n1 += 1
                n2 = n1+1