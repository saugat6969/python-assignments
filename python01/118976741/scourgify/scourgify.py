import sys
import csv
def main():
    command_line()
    output=[]
    try:
           with open(sys.argv[1]) as file:
             reader = csv.DictReader(file)
             for row in reader:
                    split_name=row["name"].split(",")

                    output.append({"first":split_name[1].lstrip(), "last": split_name[0],"house":row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read (sys.argv[1])")
    with open(sys.argv[2],"w") as file:
        writer=csv.DictWriter(file,fieldnames=["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for row in output:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})




def command_line():
    if len(sys.argv) <3 :
        sys.exit("too less argument")
    if len(sys.argv) >3:
        sys.exit("too many argument")
    if ".csv" not in (sys.argv[1] and sys.argv[2]):
        sys.exit("not a csv file")




if __name__=="__main__":
    main()

