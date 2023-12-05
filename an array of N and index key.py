



a = [10, 20, 30, 40, 50]

re = a[2]

print(re)



# Function to calculate the sum of integers in an array


# Input the number of integers
n, key= map(int, input("Enter the number of integers: ").split())

# Input the array of integers
arr = list(map(int, input("Enter the integers separated by space: ").split()))

if key >= 0 and key < n:
    print(" Element at index ",key ,"is ", arr[key])
else:
    print("Invalin index")



