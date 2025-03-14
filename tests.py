def decode(s):
    data = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        data.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return data