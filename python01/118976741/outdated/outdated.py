# months=[
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# while True:
#     date=input("enter date: ")
#     try:
#        month, day, year=date.split("/")
#        if(int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31) :
#            break
#     except:
#         try:
#            o_month,o_day,o_year=date.split(" ")
#            for i in range(len(months)):
#                if o_month==months[i]:
#                    month=i+1

#            day=o_day.replace("," , " ")
#            if (int(month)>=1 and int(month)<=12)and(int(day)>=1 and int(day)<=31):
#               break

#         except:

#             pass

# print(f"{year}-{int(month):02}-{int(day):02}")
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Enter date: ")
    try:
        # Handling the "MM/DD/YYYY" format
        month, day, year = date.split("/")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except ValueError:
        try:
            # Handling the "Month Day, Year" format
            o_month, o_day_year = date.split(" ", 1)
            for i in range(len(months)):
                if o_month == months[i]:
                    month = i + 1
                    break
            o_day, year = o_day_year.split(",")
            day = o_day.strip()
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except (ValueError, IndexError):
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

