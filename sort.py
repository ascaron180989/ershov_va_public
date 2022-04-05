def test(func):
    l1 = [[1, 2, 3, 4, 5], [2, 5, 1, 4, 3]]
    l2 = [[1, 2, 2, 2, 4, 5, 5, 5], [5, 5, 1, 2, 2, 2, 4, 5]]
    l3 = [[-100, -10, -1, 0, 1, 10, 100], [100, -100, 10, -10, 1, -1, 0]]
    l4 = [[0, 0, 0, 1], [0, 1, 0, 0]]

    print('Tests: ', end=' ')
    for x, y in l1, l2, l3, l4:
        if x == func(y):
            print('Ok', end=' ')
        else:
            print('Fail', end=' ')
    print()


def insert_sort(l):
    for i in range(1, len(l)):
        while i > 0 and l[i - 1] > l[i]:
            l[i - 1], l[i] = l[i], l[i - 1]
            i -= 1
    return l


def choice_sort(l):
    for i in range(len(l) - 1):
        m = i
        for j in range(i + 1, len(l)):
            if l[m] > l[j]:
                m = j
        if m != i:
            l[i], l[m] = l[m], l[i]
    return l


def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def merge_sort(l):
    def merge(x, y):
        i, j, s = 0, 0, []
        while True:
            if x[i] < y[j]:
                s.append(x[i])
                i += 1
                if len(x) == i:
                    s.extend(y[j:])
                    break
            else: # x[i] > y[j]
                s.append(y[j])
                j += 1
                if len(y) == j:
                    s.extend(x[i:])
                    break
        return s

    if len(l) == 1:
        return l

    d = len(l) // 2

    left = merge_sort(l[:d])
    right = merge_sort(l[d:])

    return merge(left, right)


test(insert_sort)
test(choice_sort)
test(bubble_sort)
test(merge_sort)
