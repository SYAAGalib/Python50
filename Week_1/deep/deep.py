# main function
def main():
    askquestion = input("What is the Answer to the Great Question of Life? and Universe. and Everything? ").strip().lower()
#pritn No
    if askquestion == "50":
        print("No")
    elif askquestion == "fifty":
        print("No")
    else:
        print("Yes")

#to run the code
if __name__ == "__main__":
    main()