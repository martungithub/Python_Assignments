def split(source, sep):
    len_sep = len(sep)
    res = []
    idx = 0
    for i in range(0, len(source)):
        if source[i:i + len_sep] == sep:
            res.append(source[idx:i])
            idx = i + len_sep
    return res
print(split("Hello world. This is Matt is this", "is"))