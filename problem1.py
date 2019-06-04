"""
给一个数组，数组内的元素是整数，找出其中重复出现过的整数，返回以这些重复的整数为元素组成的新数组，顺序无所谓。
例如，给定[4,3,2,7,8,2,3,1,2]，应该返回[2,3]或者[3,2]
"""


def find_dup(items: list) -> list:
    dup_times_dict = {}  # 纪录每个数字的重复次数
    dup_nums = []

    # 每遇到一次则 +1
    for i in items:
        try:
            dup_times_dict[i] += 1
        except: 
            dup_times_dict[i] = 1

    # 找出重复次数大于 1 的项
    for k, v in dup_times_dict.items():
        if v > 1:
            dup_nums.append(k)
    
    return dup_nums

# 不要修改下面的部分
if __name__ == "__main__":
    result = find_dup([4, 3, 2, 7, 8, 2, 3, 1, 2])
    assert result == [2, 3] or result == [3, 2]
    print("OK")

