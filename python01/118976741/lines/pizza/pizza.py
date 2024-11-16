import sys
from tabulate import tabulate
import csv
def main():

  command_line_check()
  table=[]
  try:
      with open(sys.argv[1],"r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            table.append(line)


  except FileNotFoundError:
     sys.exit("file doesnt exist")

  print(tabulate(table[1:],headers=table[0],tablefmt="grid"))

def command_line_check():
    #check how many element in it
    if len(sys.argv)>2:
        sys.exit("too many argument")
    if len(sys.argv)<2:
        sys.exit("too less argument")

    #csv file or not
    if ".csv" not in sys.argv[1]:
        sys.exit("NOT a csv file")

if __name__=="__main__":
    main()
