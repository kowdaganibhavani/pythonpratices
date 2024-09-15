def lists(nums):
 
  count = 0

  for num in nums:
   
    if num == 4:
   
      count = count + 1

  return count


print(lists([1, 4, 6, 7, 4])) 