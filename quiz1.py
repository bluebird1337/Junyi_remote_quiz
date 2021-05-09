def reverse_string1(s):
    new_str = ""
    length = len(s)
    for i in range(length):
        new_str += s[length-1-i]
    return new_str


print(reverse_string1("junyiacademy"))


def reverse_string2(s):
    length = len(s)
    tmp = ""
    res = ""
    for i in range(length):
        c = s[i]
        if c == ' ':
            res += reverse_string1(tmp)
            res += ' '
            tmp = ""
        elif i == length - 1:
            tmp += c
            res += reverse_string1(tmp)
        else:
            tmp += c
    return res


print(reverse_string2("flipped class room is important"))
