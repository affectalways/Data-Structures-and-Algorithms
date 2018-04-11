# -*- coding:UTF-8 -*-


# 归并排序
def merge_sort(data):
    # len(data)<=1很重要
    if len(data) <= 1:
        return data
    num = len(data) // 2
    # 递归进行排序, 最后就是一个与另一个比，比完就回馈到上层
    data_left = merge_sort(data[:num])
    data_right = merge_sort(data[num:])
    return merge(data_left, data_right)


# 归并
def merge(data_left, data_right):
    start, end = 0, 0
    result = []
    while start < len(data_left) and end < len(data_right):
        if data_left[start] <= data_right[end]:
            result.append(data_left[start])
            start += 1
        else:
            result.append(data_right[end])
            end += 1
    # 可能data_left或data_right中剩下了一些元素
    result.extend(data_left[start:])
    result.extend(data_right[end:])
    return result


if __name__ == "__main__":
    data = [9, 2, 2, 1, -1, 11, 44, 6, 7, 8, 2, 6, 2, 3, 1, 5, 0, 6, 9, 5]
    result = merge_sort(data)
    print result
