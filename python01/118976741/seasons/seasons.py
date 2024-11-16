from datetime import date
import re
import sys
import inflect
p=inflect.engine()
def main():

    dob=input("date of birth: ")
    try:
        year, month, day=check_date(dob)
    except:
        sys.exit("invalid")

    birthdate=date(int(year),int(month),int(day))
    today_date=date.today()
    dif =today_date - birthdate
    minute=dif.days*24*60
    words=p.number_to_words(minute,andword="")
    print(words.capitalize(),"minutes")


def check_date(dob):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",dob):
         year, month, day =dob.split("-")
         return year,month,day



if __name__ == "__main__":
    main()
