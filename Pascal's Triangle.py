list_pascal = []


def pascal(num):
    for i in range(num + 1):
        list_pascal.append(list([1] * (i + 1)))
        for m in range(1, len(list_pascal[i]) - 1):
            list_pascal[i][m] = list_pascal[i - 1][m - 1] + list_pascal[i - 1][m]


n = int(input())
pascal(n)
print(list_pascal[n])
