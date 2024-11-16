ask=input(" What is the answer to the Great Question of Life, the Universe and Everything? ")

if ask=="42":
    print("yes")
elif ask.lower().strip()=="forty-two":
    print("yes")
elif ask.lower().strip()=="forty two":
    print("yes")
else:
    print("No")

