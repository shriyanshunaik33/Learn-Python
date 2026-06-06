item = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for i in item:
    if i in unique_item:
        print("Duplicate: ",i)
        break
    unique_item.add(i)
