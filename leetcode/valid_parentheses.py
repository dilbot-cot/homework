class Solution:
    def isValid(self, s: str) -> bool:
        # Initialise empty list
        list = []
        # map each closing braket to corresponding opening bracket
        brackets = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        # Loop through each character in the string
        for c in s:
            # if the charater is a bracket key
            if c in brackets:
                # get the last character in the list, and if no characters exist insert placeholder
                last = list[-1] if list else '#'
                # remove the last character in the list
                list = list[:-1] if list else list
                # check if the last character does not match the value of the key in brackets, and return false
                if brackets[c] != last:
                    return False
            # if the character is not a bracket key, append it to the list
            else:
                list.append(c)
        # if there is a list, return true
        return not list