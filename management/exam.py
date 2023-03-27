def series(n, n0, dn0):
    for i in range(n + 1):
        print(n0 + 2 * i, end = ' ')

    print('')
    dn0 += n+1
    n0  += dn0
    n += 1
    if n < 4:
        series(n, n0, dn0)

series(0, 1, 2)