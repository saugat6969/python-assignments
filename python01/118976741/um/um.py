import re



def main():
    print(count(input("Text: ")))


def count(s):
    finding=re.findall(r"\bum\b[\W]?",s,re.IGNORECASE)
    return len(finding)





if __name__ == "__main__":
    main()
