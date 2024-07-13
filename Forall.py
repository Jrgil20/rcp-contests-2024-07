def complejidad(num):
    if num == 0:
        return 0
    elif num > 11111:
        if num // 11111:
            return 5 + complejidad(num // 11111) + complejidad(num % 11111)
        else:
            return 5 + complejidad(num % 11111)
    elif num > 1111:
        if num // 1111 != 1:
            return 4 + complejidad(num // 1111) + complejidad(num % 1111)
        else:
            return 4 + complejidad(num % 1111)
    elif num > 111:
        if num //111 != 1:           
            return 3 + complejidad(num // 111) + complejidad(num % 111)
        else:
            return 3 + complejidad(num % 111)
    elif num > 11:
        if num // 11 != 1:
            return 2 + complejidad(num //11 ) + complejidad(num % 11)
        else:
            return 2 + complejidad(num % 11)
    elif num == 3:
        return 3
    elif num % 3 == 0:
        return complejidad(num // 3) +3
    elif num == 2:
        return 2
    elif num % 2 == 0:
        return  complejidad(num // 2) +2
    elif num == 1:
        return 1
    else:
        return 1 + complejidad(num - 1)



num = int(input())
if 0 < num < 100000:
    result = complejidad(num)
    print(result)