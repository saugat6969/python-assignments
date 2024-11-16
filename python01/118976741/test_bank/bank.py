


def main():
    answered=input(str("Greeting:"))
    price=value(answered)
    print(price)

def value(greeting):
    if "hello" in greeting.lower().strip():
        return 0

    elif "h"==greeting.lower().strip()[0]:
         return 20
    else:
        return 100



if __name__ == "__main__":
    main()
