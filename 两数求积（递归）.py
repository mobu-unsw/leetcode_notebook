class Solution:
    def multiply(self, A: int, B: int) -> int:
        s= 0
        if B == 1:
            return A
        s+= self.multiply(A,B-1)

        return s+A
a = Solution()
print(a.multiply(A=2,B=2))
print(1>>1)
#%%
# 少年，乘法器的原理懂不懂？
# 什么？不懂？那教不了(大误。
# 把问题再简化一下，手工算乘法怎么算？十进制那种，在纸上算那种。
# 十进制能算，那么二进制能不能算呢？当然是可以的。
# 假如A=1101,B=1001。
# 怎么算呢？我们把A*B展开。
# A*B=A*1*2^3+A*0*2^2+A*0*2^1+A*1*2^0=A<<3+A<<0;
# 乘法神奇地消失了。
# 我们想办法把这个过程用代码表达出来。以下是未精简的C代码。
#
# C
#
# int multiply(int A, int B){
#     if(B){//B非0才能算
#         //从0阶(A*(B&1)*2^0)开始，每次算当前阶(A*(B&1)*2^n)的乘法并累加起来,算到B为0为止。
#         if(B&1){//如果B的最后一位是1
#             return multiply((long long)A<<1,B>>1)+A;//把B的阶放到A上去，递归算B的倒数第2位和A的乘法,然后+A。
#         }else{
#             return multiply((long long)A<<1,B>>1);//把B的阶放到A上去，递归算B的倒数第2位和A的乘法,然后+0。
#         }
#     }
#     return 0;
# }
# 然后用三目运算符，再简化一下代码，就变成了一行AC的结果了。是不是非常简单？

class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B == 0 :
            return 0
        else:
            if B&1:
                return (self.multiply(A<<1,B>>1)+A)
            else:
                return (self.multiply(A << 1, B >> 1))
a = Solution()
print(a.multiply(A=500,B=100))