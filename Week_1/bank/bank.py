def main():
#user input
    greetings = input("Greetings: ").strip().lower()
    if greetings[0:5] == "hello":
        print("$0")
    elif greetings[0] == "h":
        print("$20")
    else:
        print("$100")
main()
