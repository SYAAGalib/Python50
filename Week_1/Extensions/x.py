def main():
    userinput = input("File Name: ").strip().lower()
#.gif
    if userinput.endswith(".gif"):
        print("image/gif")
#.jpg
    elif userinput.endswith(".jpg"):
       print("image/jpeg")
#.jpeg
    elif userinput.endswith(".jpeg"):
        print("image/jpeg")
#.png
    elif userinput.endswith(".png"):
        print("image/png")
#.pdf
    elif userinput.endswith(".pdf"):
        print("application/pdf")
#.txt
    elif userinput.endswith(".txt"):
        print("text/plain")
#.zip
    elif userinput.endswith(".zip"):
        print("application/zip")
#else
    else:
        print("application/octet-stream")
if __name__ == "__main__":
    main()