#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([x**2 for x in nums])
    runs in n log nonlocalbut maybe we want n time complexity
    or 

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0 
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.insert(0, nums[left]**2)
                left += 1
            else:
                result.insert(0, nums[right]**2)
                right -= 1
        return result