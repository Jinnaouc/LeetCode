class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        for i,item in enumerate(nums):
            a.append(i)
            annum = target - item
            nums2 = nums[i+1:]
            if annum in nums2:
                a.append(nums2.index(annum)+i+1)
                break
            a = []
        return a
