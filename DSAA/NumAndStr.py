#数字转换为字符串的全排列
def trasf(num_str, i):
    if i == len(num_str):
        return 1
    if num_str[i] == '0':
        return 0
    if num_str[i] == '1':
        res = trasf(num_str, i+1)
        if i < len(num_str) - 1:
            res += trasf(num_str, i+2)
        return res
    if num_str[i] == '2':
        res = trasf(num_str, i+1)
        if i < len(num_str) - 1 and num_str[i+1] < '7':
            res += trasf(num_str, i+2)
        return res
    return trasf(num_str, i+1)

n = '1111'
print(trasf(n, 0))
