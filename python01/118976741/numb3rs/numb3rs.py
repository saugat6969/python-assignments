import re
import sys


def main():
    address=input("IPv4 Address: ")
    valid=validate(address)
    print(valid)



def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$" ,ip):
        lists=ip.split(".")
        for list in lists:
            if int(list)<0 or int(list)>255:
                return False
        return True
    else:
        return False







if __name__ == "__main__":
    main()
