# n = int(input())
# sum_fac = 0
# f = 1
# for i in range(1, n + 1):
#     f = f * i
#     sum_fac += f
# print(sum_fac)
# 0,8
#2
# a = [int(i) for i in input().split()]
# max_index = a.index(max(a))
# min_index = a.index(min(a))
# a[max_index], a[min_index] = a[min_index], a[max_index]
# print(a)
# 1,5
#4
# n = int(input())
# a = {}
# for i in range(n):
#     b = input()
#     if b not in a:
#         a[b] = 1
#     else:
#         a[b] = a.get(b) + 1
# s = max(a.values())
# for el in a.items():
#     if el[1] == s:
#         print(el[0])
# 1,7


# n = int(input())
# a = [[1] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i + j < n - 1:
#             a[i][j] = 0
#         elif i + j > n - 1:
#             a[i][j] = 2
# for el in a:
#     print(*el)


