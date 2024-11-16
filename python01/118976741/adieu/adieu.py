# import inflect
# p=inflect.engine()
# try:
#    names=[]
#    while True:
#      name=input("Names :").capitalize()
#      names.append(name)
# except EOFError:
#    pass

# print (names)
# joined_names=p.join(names)
# print(f"Adieu,adieu, to {joined_names}")



import inflect

# Create an engine
p = inflect.engine()

try:
    names = []
    print("Enter names (press Ctrl+D to finish):/n")
    while True:
        name = input("Names: ").capitalize()

        names.append(name)

except EOFError:
    print("/n")
    pass

# Output the names

joined_names = p.join(names)
print(f"Adieu, adieu, to {joined_names}")
