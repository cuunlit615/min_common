def min_common(a, b):
    ans = []
    if len(a) > len(b):
        l1, l2 = b, a
    else:
        l1, l2 = a, b
    for n in l1:
        if n in l2:
            ans.append(n)
    if ans:
        ans.sort()
        return ans[0]
    else:
        return []


def s_into_i(inp):
    lc =[]
    for n in inp:
        lc.append(int(n))
    return lc


def nums_check(st):
    if st.isdigit:
        return st


def main():
    na = s_into_i(nums_check(input('nums1')))
    nb = s_into_i(nums_check(input('nums2')))
    return min_common(na, nb)


print(main())
