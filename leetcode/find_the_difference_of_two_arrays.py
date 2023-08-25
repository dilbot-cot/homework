class Solution:
    def findDifference(self, nums1, nums2):
        #convert both lists into sets, this removes duplicated numbers
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        #subtract set_num2 from set_nums1, turn this back into a list
        #do the same for set_nums2
        answer_0 = list(set_nums1 - set_nums2)
        answer_1 = list(set_nums2 - set_nums1)
        #put the answer into descired output
        answer = [answer_0, answer_1]

        return answer