

# Given an sorted array A of size N. Find number of elements which are less than or equal to given
# element X

#  Input:
# N = 7
# A[] = {1, 2, 2, 2, 5, 7, 9}
# X = 2
# Output:
# 4



def count_elements_less_than_or_equal_to(arr, x):
      n = len(arr)

      left, right = 0, n - 1
      while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= x:
                 left = mid + 1
            else:
                  right = mid - 1




      return left


arr = [1, 2, 2, 2, 5, 7, 9]
x = 2

result = count_elements_less_than_or_equal_to(arr, x)

print(result)


### Different solution using bisect module

from bisect import  bisect_right

def count_elements_less_than_or_equal_to_1(arr1, x1):
      return bisect_right(arr1, x1)

arr1 = [1, 2, 2, 2, 5, 7, 9]

x1 = 6

get_result = count_elements_less_than_or_equal_to_1(arr1, x1)

print(get_result)

