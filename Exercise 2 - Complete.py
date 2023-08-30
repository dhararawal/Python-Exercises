# Declare the variables
a, b, i, j, flag = 0, 0, 0, 0, 0

# Ask user to input the first positive integer
print("Enter the 1st positive integer:", end="")
a = int(input())
print(a)

# Ask user to input the second positive integer
print("Enter the 2nd positive integer:", end="")
b = int(input())
print(b)

#Arrange the users number so the smaller number is picked as the lower bound interval
#Arrange the uers number so the larger number is picked as the upper bound interval
if a > b:
    higher = a
    lower = b
else:
    higher = b
    lower = a

# Print display message
print("The prime numbers between", lower, "and", higher, "are: ", end="")

# Use a for loop to go through all numbers in the given interval
for i in range(lower, higher + 1):
    # Skip 1 as 1 is not a prime number
    if (i == 1):
        continue

    # flag variable if i is a prime number or not
    flag = 1

    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 0
            break

        # flag = 1 means i is prime number
        # flag = 0 means i is not prime number
    if (flag == 1):
        print(i, end=" ")