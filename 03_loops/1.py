numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

positive = 0
negetive = 0
for num in numbers:
    if num>0:
        positive += 1
    else:
        negetive += 1

print("No. of positive numbers ",positive)
print("No. of negetive numbers ",negetive)

