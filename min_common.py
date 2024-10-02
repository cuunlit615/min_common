a = [1, 2, 3, 4, 5, 6]
b = [9, 6, 4, 19, 7]
ans = []


def min_common(l1, l2):
    for n in l1:
        if n in l2:
            ans.append(n)
    ans.sort()
    return ans[0]


print(min_common(a, b))
