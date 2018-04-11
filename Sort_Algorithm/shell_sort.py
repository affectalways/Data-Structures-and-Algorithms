# -*- coding:UTF-8 -*-

def shell_sort(unsort_data):
    data_len = len(unsort_data)
    gap = data_len // 2

    while gap > 0:
        for i in range(gap, data_len):
            for j in range(i, 0, -gap):
                if j >= gap:
                    if unsort_data[j] < unsort_data[j - gap]:
                        unsort_data[j], unsort_data[j - gap] = unsort_data[j - gap], unsort_data[j]
        gap = gap // 2

    return unsort_data


if __name__ == "__main__":
    unsort_data = [7, 8, 2, 6, 2, 3, 1, 5]
    print shell_sort(unsort_data=unsort_data)
