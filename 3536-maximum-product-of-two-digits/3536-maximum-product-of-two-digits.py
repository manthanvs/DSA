class Solution:
    def maxProduct(self, n: int) -> int:
        # sorted(str(n)) we would get digits in sorted str. 
        # then we would get the last two digits. [-2:] start from -2.. start from second last digit.  
        d1, d2 = sorted(str(n))[-2:]
        
        # simply use those two maximum digit string into product.
        return int(d1) * int(d2)