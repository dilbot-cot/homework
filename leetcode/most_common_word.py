import re
from collections import Counter

class Solution:
    def mostCommonWord( paragraph, banned):
        # initialise an empty list to store the new list after removing banned words
        p_list = []
        # replace all special characters with whitespace, make the text lower case and split the string into a list where there is white space
        p_clean = re.sub(r'[^a-zA-Z0-9 ]', ' ', paragraph.lower()).split()
        # for each element in the list
        for c in p_clean:
            # if the element is not in the banned words, append it to the empty list
            if c not in banned:
                p_list.append(c)
        # perform a count operation to build a dict of each element and frequency
        words = Counter(p_list)
        # return the 1 most common response, and provide me the key of the dict
        common = words.most_common(1)[0][0]
        return common