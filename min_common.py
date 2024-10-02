def s_into_i(st):
    ints = []
    if isinstance(st, str):
        for s in st:
            ints.append(s)
        return ints
    else:
        return st


def min_common(l1, l2):
    ans_mc = []
    for n in l1:
        if n in l2:
            ans_mc.append(n)
    ans_mc.sort()
    return ans_mc[0]


def main(inp1, inp2):
    inp1 = s_into_i(a)
    inp2 = s_into_i(b)
    ans_m = min_common(inp1, inp2)
    return ans_m


a = [1, 2, 3, 4, 5, 6]
b = [9, 6, 4, 19, 7]

print(main(a, b))
