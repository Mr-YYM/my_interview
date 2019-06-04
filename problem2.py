"""
写一个函数将 ipv4 地址字符串 (仅包含数字，点) 转化成 32 位整数，要求输出合法地址的 32 位整型结果。
"""

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
    four_nums = map(int, address.split('.'))
    four_nums_binary = list(map(decimal_to_binary, four_nums))
    four_nums_binary_8bit = [(8-len(num))*'0'+num for num in four_nums_binary]
    xxx = ''.join(four_nums_binary_8bit)


# 不要修改下面的部分
if __name__ == "__main__":
    assert ipv4_to_int("0.0.0.0") == 0
    assert ipv4_to_int("192.168.0.0") == 3232235520
    assert ipv4_to_int("255.255.255.255") == 4294967295
    print("OK")
