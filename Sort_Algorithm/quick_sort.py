# -*- coding:UTF-8 -*-


# 快速排序，应叫做quick_sort
def fast_sort(data, start, end):
    if start >= end:
        return data

    # 选取data的第一个点作为切分点
    print 'cutting_point'
    cutting_point = data[start]
    print cutting_point

    left = start
    right = end

    # 一定要先右边，再左边，否则排序一直不对
    while left < right:
        while left < right and data[right] >= cutting_point:
            right -= 1
        while left < right and cutting_point >= data[left]:
            left += 1

        if left < right:
            data[left], data[right] = data[right], data[left]

    data[start] = data[left]
    data[left] = cutting_point

    fast_sort(data=data, start=start, end=left - 1)
    fast_sort(data=data, start=left + 1, end=end)


if __name__ == "__main__":
    data = [9, 2, 2, 1, -1, 11, 44, 6, 7, 8, 2, 6, 2, 3, 1, 5, 0, 6, 9, 5]
    fast_sort(data=data, start=0, end=len(data) - 1)
    print data
