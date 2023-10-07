def main():
    tweet = input("What's on your mind? ")
    print(vowel_remove(tweet))


def vowel_remove(post):
    vowel = "AEIOUaeiou"
    result = ""
    for char in post:
        if char not in vowel:
            result += char
    return result

if __name__ == '__main__':
    main()
