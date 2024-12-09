# вывести числа Фибоначчи
#
# N = int(input())
#
# def fib(n):
#     lst = [0, 1]
#     for i in range(2, n):
#         lst.append(lst[i-2] + lst[i-1])
#     print(*lst)
#
#
# fib(N)


# бинарный поиск

# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# N = lst1[0]
# K = lst2[0]
# lst1 = lst1[1:]
# lst2 = lst2[1:]
#
#
# def binary_search(array, n):
#     l = 0
#     r = len(array)
#     while l + 1 < r:
#         m = (l + r) // 2
#         if array[m] > n:
#             r = m
#         elif array[m] < n:
#             l = m
#         else:
#             return m + 1
#     if array[l] == n:
#         return l + 1
#     return -1
#
#
# def indexes_search(array, array_desired):
#     result = []
#     for i in range(len(array_desired)):
#         result.append(binary_search(array, array_desired[i]))
#     return result
#
#
# print(*indexes_search(lst1, lst2))
#



# лестница

N = int(input())
lst = list(map(int, input().split(" ", N)))


def upstairs(array):
    step = array[0]
    step_prev = 0
    for i in array[1:]:
        t = step_prev
        step_prev = step
        step = max(t, step) + i
    return step


print(upstairs(lst))
