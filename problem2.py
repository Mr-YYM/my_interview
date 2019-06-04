"""
写一个函数将 ipv4 地址字符串 (仅包含数字，点) 转化成 32 位整数，要求输出合法地址的 32 位整型结果。
"""

# 将十进制的整数转换成字符串形式的二进制数
def decimal_to_binary(decimal_num: int) -> str:
    binary_num = ''
    while decimal_num > 0:
        r = decimal_num % 2
        decimal_num = decimal_num // 2
        binary_num = str(r) + binary_num
    if binary_num == '':
        return '0'
    return binary_num


def ipv4_to_int(address: str) -> int:
    four_nums = map(int, address.split('.'))  # 提取出IP中的4个数 [192,168,31,1]
    four_nums_binary = map(decimal_to_binary, four_nums)  # 全部转换成二进制表达 [11000000,10101000,11111,1]
    four_nums_binary_8bit = [(8-len(num))*'0' + num for num in four_nums_binary]  # 给不满8位的那些数前补充足够的0 [11000000,10101000,00011111,00000001]
    num_8bit = ''.join(four_nums_binary_8bit)  # 四个二进制数结合在一起 '11000000101010000001111100000001'

    result = 0
    for i in range(32):
        if num_8bit[i] == '1':
            result += 2**(31-i)
        elif num_8bit[i] == '0':
            continue
    
    return result


# 不要修改下面的部分
if __name__ == "__main__":
    assert ipv4_to_int("0.0.0.0") == 0
    assert ipv4_to_int("192.168.0.0") == 3232235520
    assert ipv4_to_int("255.255.255.255") == 4294967295
    print("OK")

