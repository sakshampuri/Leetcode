#reversing a 32 bit signed integer
class Solution:
    def reverse(self, x: int) -> int:
        y:int=0
        flag = False
        if x < 0:
            flag = True
            x *= -1
        while x > 0:
            y = y*10+x%10
            if y < -2**31 or y > 2**31:
                return 0
            x = int(x/10)
        
        return y if flag == False else -y 

print(Solution().reverse(-32411))
