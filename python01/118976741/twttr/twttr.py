def main():
    output=""
    vowels="aeiouAEIOU"
    woym=str(input("Input:"))
    for char in woym:
        if char not in vowels:
           output+=char
    print("Output:",output)

main()
