# def convert(text):
#          text=text.replace(":)","😊").replace(":(","😟")
#          return text
# def main():
#     user_input=(input("enter string:"))
#     print(convert(user_input))


# main()
def main():
    user_input = input("")
    converted_str = convert(user_input)
    print(converted_str)
def convert(user_input):
    # Replace :) with 😊 and :( with ☹️
    user_input1 = user_input.replace(":)", "🙂")
    user_input2 = user_input1.replace(":(", "🙁")
    return user_input2



if __name__ == "__main__":
    main()
