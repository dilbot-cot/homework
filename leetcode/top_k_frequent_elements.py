from collections import Counter # imports a module that is a dict subclass for counting objects

class Solution:
    def topKFrequent(self, nums, k: int):
        #Count the frequency of each number in the array
        freq = Counter(nums)
        #sort each number based on frequency, the optional argument key=lambda x: freq[x] completes this task
        sorted_num = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        #pick the first k elements
        result = sorted_num[:k]
        return result