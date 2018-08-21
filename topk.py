numbers = [5, 6, 2, 3, 4, 8, 7, 9, 1, 23, 22, 11, 5, 2, 9, 3, 44, 22, 88, 31, 98, 24, 56, 23, 77]
length = len(numbers)
k = 5


def swap(i, j):
    """
    交换元素
    :param i:
    :param j:
    :return:
    """
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp


def adjust(i, n):
    """
    从某个节点开始向下调整
    :param i:
    :param n:
    :return:
    """
    j = i * 2 + 1
    while j < n:
        if j + 1 < n and numbers[j + 1] < numbers[j]:
            j += 1
        
        if numbers[j] < numbers[i]:
            swap(i, j)
        
        i = j
        j = i * 2 + 1


def create():
    """
    创建堆
    :return:
    """
    init = int((k + 1) / 2) - 1
    for i in range(init, -1, -1):
        adjust(i, k)


def top_k():
    """
    排序
    :return:
    """
    # 构建堆
    create()
    # 排序过程，大顶堆调整
    for i in range(k, len(numbers)):
        if numbers[i] > numbers[0]:
            swap(i, 0)
            adjust(0, k)
    return numbers[:k]


def sort():
    """
    排序
    :return:
    """
    # 构建堆
    create()
    # 排序过程，大顶堆调整
    i = length - 1
    while i >= 0:
        swap(i, 0)
        adjust(0, i)
        i -= 1


result = top_k()
print(result)
