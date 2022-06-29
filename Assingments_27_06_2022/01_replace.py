def split(source, old, new , count=None):
    counter = 0
    if count is None:
        count = source.count(old)
    for i in range(len(source)):
        if counter < count:
            low_index = source.find(old)
            high_index = low_index + len(old)
            source = source[:low_index] + new + source[high_index:]
            counter += 1
    print(source)


split("Hello world. This is Matt is this","is","are")
