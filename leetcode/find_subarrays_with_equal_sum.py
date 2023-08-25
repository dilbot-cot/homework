class Solution:
    def findSubarrays(self, nums) -> bool:
        #get the total length of the list
        list_length = len(nums)

        #break this into subarrays of total length 2
        #compare the subarrays and if any are equal return result of True
        #loop
        for i in range (list_length - 1):
            for j in range (i + 1, list_length - 1):
                sum1 = sum(nums[i:i+2])
                sum2 = sum(nums[j:j+2])
                if sum1 == sum2:
                    return True
        return False