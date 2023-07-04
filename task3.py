from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums.count(nums[i]) == 1:
                return nums[i]

if __name__=='__main__':
    obj = Solution()
    print(obj.singleNumber(nums=[1,2,4,1,2]))