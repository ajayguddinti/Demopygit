# *
# * *
# * * *
# * * * *
# * * * * *

# Print the "*" for 5 rows

row = 1

for i in range(row, 6):
    for j in range(i):
       print("*", end="")
       row += 1
    print()

print('\n Code using with While loop')
#####
i = 1
while i < 6:
    product = "$" * i
    print(product)
    i += 1


print('\n')

i = 1
for i in range(i, 6):
    for j in range(i):
        if i < 6:
            product = "@" * i
            print(product)
        i += 5













