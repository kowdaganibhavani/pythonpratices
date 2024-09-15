def member(data, n):
   
    for value in data:
        if n == value:
            return True  
    return False  
print(member([1, 5, 8, 3], 3))  
print(member([5, 8, 3], -1))    