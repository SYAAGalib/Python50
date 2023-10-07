def main():
    grand_total = 0
    while True:
        try:
            order = input("Item:").title()
            if menu(order) is not None:
                grand_total += menu(order)
                print("Total: $", end="")
                print("{:.2f}".format(grand_total))
        except EOFError:
            print()
            break


def menu(key):
    item = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    if key not in item:
        return None
    return item.get(key)


if __name__ == "__main__":
    main()
