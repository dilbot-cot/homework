class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        decimal = a_int + b_int
        binary = []
        if decimal == 0:
            return '0'
        while decimal > 0:
            remainder = decimal % 2
            binary.append(str(remainder))
            decimal //= 2
        binary_string = "".join(binary[::-1])
        return binary_string