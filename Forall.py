def complejidad (num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    if num % 11 == 0:
        return 1 + complejidad(num // 11)

    if num > 11:
        if num % 10 == 0:
            return 1 + complejidad(num % 11)
        return 1 +complejidad(num % 10)
    
    if num == 2:
        return 2
    if num % 2 == 0:
        return 2 + complejidad(num//2)
    
    if num == 3:
        return 3
    if num % 3 == 0:
        return 3 + complejidad(num//3)
    
    return 1 + complejidad(num-1)

num = int(input())
if num > 0 or num < 1000000:
    result = complejidad(num)
print(result)

