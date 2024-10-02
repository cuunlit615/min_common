def min_common(a, b):
    ans = []
    if len(a) > len(b):
        l1, l2 = b, a
    else:
        l1, l2 = a, b
    for n in l1:
        if n in l2:
            ans.append(n)
    ans.sort()
    return ans[0]


a = [2, 9, 4, 19, 7]
b = [9, 6, 4, 19, 7]
c = ['2', '5']

print(min_common(a, b))
