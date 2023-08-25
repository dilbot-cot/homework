class Solution:
    def majorityElement(self, nums) -> int:
        # Put the numbers in order
        nums.sort()
        # get the legth of the list
        n = len(nums)
        # We are searching for the majority, (more than 50%), not the most common.
        # we can return the number that appears at the middle position of the sorted list.
        return nums[n//2]