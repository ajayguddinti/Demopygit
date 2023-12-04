

x = [ 1, 2, 3, 4]

re = sum(x)

print(re)

#Input:
#6
#5 8 3 10 22 45
#Output:
#93

x = [ 5, 8, 3, 10, 22, 45]

re = sum(x)

print(re)


# Function to calculate the sum of integers in an array
def calculate_sum(arr):
    return sum(arr)

# Input the number of integers
n = int(input("Enter the number of integers: "))

# Input the array of integers
arr = list(map(int, input("Enter the integers separated by space: ").split()))

# Calculate and print the sum
result = calculate_sum(arr)
print("Sum of integers:", result)
