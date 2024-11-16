

def main():

    woym=str(input("Input:"))
    without_vowels=shorten(woym)
    print("output:",without_vowels)


def shorten(word):
     output=""
     vowels="aeiouAEIOU"
     for char in word:
        if char.lower() not in vowels:
           output+=char
     return output



if __name__ == "__main__":
    main()
