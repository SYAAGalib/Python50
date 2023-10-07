#input
def main():
    words = input()
    print(replace(words))

#replace :) / :(
def replace(words):
    words = words.replace(":)","🙂").replace(":(","🙁")
    return words

main()