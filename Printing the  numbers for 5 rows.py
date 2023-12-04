

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# Print the above formate number triangle

current_value = 1
rows = 8

for i in range(1, rows + 1):
    for j in range(i):
        print(current_value, end='')
        current_value += 1
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
#Print the above formate of trangle


rows = 6

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

