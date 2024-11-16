def main():
    camel_case_input=input("camelCase: ")
    snake_case_out=camel_to_snake(camel_case_input)
    print("snake_case: ",snake_case_out)


def camel_to_snake(camel_case):
    snake_case=" "

    for char in camel_case:
        if char.isupper():
            snake_case +='_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')


main()

