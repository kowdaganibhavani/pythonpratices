def sums(x, y, z):
    
    if x == y or y == z or x == z:
        sum = 0
    else:
        
        sum = x + y + z
    
    return sum

print(sums(2, 1, 2))