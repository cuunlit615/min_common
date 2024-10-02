a = [1, 2, 3, 4, 5, 6]
b = [9, 6, 4, 19, 7]
ans =[]
for n in a:
    if n in b:
        ans.append(n)
ans.sort()

print(ans[0])
