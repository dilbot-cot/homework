class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_list = []
        for c in s:
            if c in char_list:
                return c
            else:
                char_list.append(c)