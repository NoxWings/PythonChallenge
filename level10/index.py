def describe(sequence):
    last = sequence[0]
    count = 0
    result = ""

    for c in sequence:
        if (c != last):
            result += "{}".format(count)
            result += "{}".format(last)
            last = c
            count = 0
        count += 1

    result += "{}".format(count)
    result += "{}".format(last)
    return result

a = ["1"]

for i in range(30):
    a2 = describe(a[-1])
    a.append(a2)

print(len(a[30]))
