def count(n):
    if n == 0:
        return 1
    r = count.cache.get(n,0)
    if r:
        return r
    for k in range(n):
        r+= count(k) * count(n-1-k)
    count.cache[n] = r
    return r
count.cache={0:1}
print(count(50))