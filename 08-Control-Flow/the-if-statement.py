def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    
    return "odd"

print(even_or_odd(0))


def negative_energy(num):
    if num >= 0:
        return num
    elif num < 0:
        return -(num)
   

print(negative_energy(0))