def main():
    fruit_asked = input("Item: ").strip().lower()

    print(fruits_in_dict(fruit_asked))

# fruits_in_dict(key) function contains a dictionary and needs an input to access.
# it returns the kew value to the main function
def fruits_in_dict(key):
    fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}
    return fruits.get(key, "")

if __name__ == "__main__":
    main()

