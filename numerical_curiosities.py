# If you multiply any number by 9 and sum digits of the result, then sum digits again and so forth, you eventually reach 9
def magic9(x, limit=100):

    i = 0
    s = str(x*9)
    print(x,"*",9,"=",s)
    while True:
        s = sum([int(digito) for digito in str(s)])
        print(s)
        if len(str(s)) == 1 or i == limit:
            break
    return s

magic9(299_792_458)
