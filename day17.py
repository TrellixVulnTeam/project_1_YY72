'''
排序算法
'''


def select_sort(items, comp=lambda x, y: x < y):
    """选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swap = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swap = True
        if not swap:
            break
    return items


def merge(items1, items2, comp=lambda x, y: x < y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def _merge_sort(items, comp):
    """归并排序"""
    if (len(items) < 2):
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(items, comp)


'''
查找
'''


def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index + 1
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    print(select_sort(list1))
    print(bubble_sort(list1))
    print(merge_sort(list1))
    print(list1)
    print(seq_search(list1, 99))
    print(bin_search(merge_sort(list1), 99))


if __name__ == '__main__':
    main()
