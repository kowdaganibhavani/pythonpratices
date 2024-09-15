age = int(input("Input a dog's age in human years: "))

if age < 0:
    print("Age must be a positive number.")
    exit()

elif age <= 2:
    age = age * 10.5

else:
    age = 21 + (age - 2) * 4

print("The dog's age in dog's years is", age) 
  
