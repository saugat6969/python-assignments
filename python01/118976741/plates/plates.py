# # def main():
# #     plate = input("Plate:").upper()
# #     if is_valid(plate):
# #         print("Valid")
# #     else:
# #         print("Invalid")


# # def is_valid(s):
# #     # Requirement 1: All vanity plates must start with at least two letters.
# #     if len(s)>2 or  s[:2].isalpha():
# #         return True
# #     # Requirement 2: Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters.
# #     if len(s)<2 or len(s)>6:
# #         return False
# #     # Requirement 3: Numbers cannot be used in the middle of a plate; they must come at the end.
# #     if not s[-1].isdigit() and ( not s[2:-1].isdigit() and s[2]!="0"):
# #         return False

# #     return True





# # main()




# def is_valid(s):
#     # Requirement 1: All vanity plates must start with at least two letters.
#     if len(s) < 2 or not s[:2].isalpha():
#         return False

#     # Requirement 2: Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters.
#     if len(s) < 2 or len(s) > 6:
#         return False

#     # Requirement 3: Numbers cannot be used in the middle of a plate; they must come at the end.
#     if (s[2:-1].isdigit()) and (s[2]!=0) and  (s[-1].isdigit()):
#         return True

#     i=0
#     while i< len(s):
#         if s[i].isaplha()==False:
#             if s[i]=='0':
#                 return False
#             else:
#                 break
#         i+=1

#     for i in range(len(s)):
#         if s[i].isdigit():
#             if not s[i].isdigit():
#                 return False


#     for c in s:
#         if c in ['.',' ',',','!','?']:
#             return False

#     # If all requirements are met, return True
#     return True


# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# main()
def main():
    plate=input("Plate:")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):

    if len(s)<2 or len(s)>6:
        return False
    if s[0].isalpha()==False or s[1].isalpha()==False:
        return False
    i=0
    while i< len(s):
        if s[i].isalpha()==False:
            if s[i]=='0':
                return False
            else:
                break
        i+=1

    for i in range(len(s)):
        if s[i].isdigit():


        #   if not s[i].isdigit():
           if s[i] == '0' and not any(c.isdigit() for c in s[:i]):
                return False



    for c in s:
        if c in ['.',' ',',','!','?']:
            return False


    return True

if __name__=="__main__":
   main()




