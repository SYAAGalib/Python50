grocery = {}

while True:
    try:
        # Get the items from the user
        item = input().upper()

        # Check if the item is already in the list
        if item in grocery:
            # If it is already in the list then quantity will increase by 1
            grocery[item] += 1
        else:
            # If the item is not in the list then it will be added to the list
            grocery[item] = 1

    except EOFError:
        print()
        break

# print the list with quantity
for item in sorted(grocery.keys()):
    print(grocery[item], item)
    