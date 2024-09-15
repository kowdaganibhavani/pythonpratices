def average(nums):
    
    result = [sum(x) / len(x) for x in zip(*nums)]
  
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

print ("Original Tuple: ")

print(nums)

print("\nAverage value of tuples:\n", average(nums))

nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

print ("\nOriginal Tuple: ")

print(nums)


print("\nAverage tuple of tuples:\n", average(nums)) 

