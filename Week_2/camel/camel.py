### user input and veriables declaration
camelCase = input("CamelCase: ")
snake_case = ""

### logic and decide the value of snake case
for i in range(len(camelCase)):

### snake case or not
    if camelCase[i].isupper():
        print(i)
        print(snake_case)
        snake_case = snake_case + '_' + camelCase[i].lower()
        print(snake_case)
    else:
        snake_case += camelCase[i]

### output
print("snake_Case: ", snake_case)