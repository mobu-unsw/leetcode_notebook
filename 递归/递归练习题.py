#相反输出字符串

str = input("输入字符串：")
def reverce(x):
    if len(x) == 0:
        return ''
    s = x[-1]
    s+= reverce(x[:-1])
    return s
print(reverce(str))
