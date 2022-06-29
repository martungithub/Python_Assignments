def split(source, sep, count=None):
    res = []
    counter = 0
    if count is None:
        count = source.count(sep)
    for i in range(len(source)):
        if counter < count:
            first = source.find(sep)
            res.append(source[:first])
            source = source[first + len(sep):]
            counter += 1
    res.append(source)
    print(res)


split("Hello world. This is Matt is this","is",1)
