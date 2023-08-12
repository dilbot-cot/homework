class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # get the list length to pass through a later range
        n = len(nums)
        # sort the numbers in the list in order so we only need to find the first time this doesn't occur
        nums_sorted = sorted(nums)
        # iterate through the range (n)
        for i in range (n):
            # if the position of i is not equal to the number of i, return this number
            if nums_sorted[i] != i:
                return i
        # in the event it passes through the range, the answer must be the last number, which is equal to the length.
        return n