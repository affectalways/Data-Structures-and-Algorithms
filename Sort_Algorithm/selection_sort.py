# -*- coding:UTF-8 -*-

def selection_sort(unsort_data):
    data_len = len(unsort_data)
    for i in range(data_len):
        for j in range(i, data_len):
            if unsort_data[i] > unsort_data[j]:
                unsort_data[i], unsort_data[j] = unsort_data[j], unsort_data[i]
    return unsort_data


if __name__ == "__main__":
    unsort_data = [7, 8, 2, 6, 2, 3, 1, 5, 0, 6, 9, 5]
    print selection_sort(unsort_data=unsort_data)
