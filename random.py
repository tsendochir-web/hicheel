# a = list(map(int, input().split()))
# a.sort()
# b = set(a)
# c = list(b)
# print(c[-2])

# a = list(map(int, input().split()))
# a.reverse()
# b = set(a)
# c = list(b)
# print(c[1])


# a = list(map(int, input().split()))#########################################################
# b = 0
# c = 0
# for i in a :
#     if i % 2 != 0 :
#         c += 1
#         b = max(b, c)
#     else : 
#         c = 0
# print(b)



# def linear(l, t):
#     for i in enumerate(len(l)):
#         if l[i] == t :
#             return i
#     return -1
# l = list(map(int, input().split()))
# t = int(input())
# r = linear(l,t)
# print(r)


def lenear(l, t):
    for x, i in enumerate(l):
        if i == t :
            return x
    return -1
l = input().split()
t = input()
print(lenear(l, t))






