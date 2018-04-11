# -*- coding:UTF-8 -*-

def insertion_sort(unsort_data):
    data_len = len(unsort_data)
    for i in range(data_len):
        for j in range(i, 0, -1):
            # j - 1 可能为-1， 每次bi最后一个比就没有意义了
            if (j - 1) < 0:
                break
            if unsort_data[j] < unsort_data[j - 1]:
                unsort_data[j], unsort_data[j - 1] = unsort_data[j - 1], unsort_data[j]

    return unsort_data


if __name__ == "__main__":
    unsort_data = [7, 8, 2, 6, 2, 3, 1, 5, 0, 6, 9, 5]
    print insertion_sort(unsort_data=unsort_data)
