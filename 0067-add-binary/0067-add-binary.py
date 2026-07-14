class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # So I used the type casting string to binary: 
        # int(a, 2) => here the following int("eg: 1001", 2) the step count is 2 therefore the following string get's converted to integer value for base 2
        # Once this integer value is calculated for both then we simply add, and then type caste back into binary=>String
        # bin() => the following type casted value would be Ob1010 something, which can be sliced from the front [2:] with slice operator

        return bin((int(a, 2)) + (int(b, 2)))[2:]