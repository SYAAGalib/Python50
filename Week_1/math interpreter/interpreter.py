x, y, z = input("Enter an arithmetic expression: ").split(" ")

if y == "+":
    ans = float(x) + float(z)
    print(ans)
elif y == "-":
    ans = float(x) - float(z)
    print(ans)
elif y == "*":
    ans = float(x) * float(z)
    print(ans)
elif y == "/":
    ans = float(x) / float(z)
    print(ans)