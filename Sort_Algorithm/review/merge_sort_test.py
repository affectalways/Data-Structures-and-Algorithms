# -*- coding:UTF-8 -*-

# 归并排序
def merge_sort(data):
    if len(data) <= 1:
        return data
    count = len(data) // 2
    left_data = merge_sort(data[:count])
    right_data = merge_sort(data[count:])
    return merge(left_data, right_data)


def merge(left_data, right_data):
    left_start, right_start = 0, 0
    result = []
    while left_start < len(left_data) and right_start < len(right_data):
        if left_data[left_start] <= right_data[right_start]:
            result.append(left_data[left_start])
            left_start += 1
        else:
            result.append(right_data[right_start])
            right_start += 1
    result.extend(left_data[left_start:])
    result.extend(right_data[right_start:])
    return result


if __name__ == "__main__":
    data = [9, 2, 2, 1, -1, 11, 44, 6, 7, 8, 2, 6, 2, 3, 1, 5, 0, 6, 9, 5]
    result = merge_sort(data)
    print result
