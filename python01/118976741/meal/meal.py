def main():
    current_time=input("what time is it(format:##:## or #:##? ")

    time=convert(current_time)
    if time>=7 and time<=8:
        print("breakfast time")
    if time>=12 and time<=13:
        print("lunch time")
    if time>=18 and time<=19:
        print("dinner time")






def convert(time):
    hours , minute =time.split(":")
    min=float(minute)/60
    return float(hours)+min





if __name__ == "__main__":
    main()
