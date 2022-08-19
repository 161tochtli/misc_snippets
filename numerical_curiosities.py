# If you multiply any number by 9 and sum digits of the result, then sum digits again and so forth, you eventually reach 9

def magic9(x, limit=100):
    
    s = x * 9
    print(x, "*", 9, "=", s)

    i = 0
    while len(str(s)) > 1 and i < limit:
        s = sum([int(digito) for digito in str(s)])
        print(s)
        i += 1


magic9(299_792_458,10)

