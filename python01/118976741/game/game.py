import random

def get_level():
    while True:
        level = input("level: ")
        if level.isdigit() and int(level) > 0:
            return int(level)
        else:
            print("Please enter a positive integer.")

def get_guess():
    while True:
        guess = input("Enter your guess (a positive integer): ")
        if guess.isdigit() and int(guess) > 0:
            return int(guess)
        else:
            print("Please enter a positive integer.")

def main():
    level = get_level()
    target_number = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()



