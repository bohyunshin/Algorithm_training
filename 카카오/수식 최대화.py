cacheSize = 3
reference = [4, 2, 3, 4, 5, 6, 5, 4, 7]
cache = []
for ref in reference:
    if not ref in cache:
        if len(cache) < cacheSize:
            cache.append(ref)
        else:
            cache.pop(0)
            cache.append(ref)
    else:
        cache.pop(cache.index(ref))
        cache.append(ref)
    print(cache)