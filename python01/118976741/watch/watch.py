import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        matches=re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9]+)",s)

        if matches:
          youtube=f"https://youtu.be/{matches.group(4)}"
          return youtube
        else:
         return None














if __name__ == "__main__":
    main()
