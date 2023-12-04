

def find_largest_number(numbers):
    if not numbers:
        return None
    else:
        return max(numbers)

number_list = [ 12, 31, 4, 66, 77, 79, 9, 7]
largest_number = find_largest_number(number_list)

if largest_number is not None:
    print(f"The largest number in list is :{largest_number}")
else:
    print("This list is empty")

