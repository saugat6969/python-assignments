import sys
def main():
    #check the command line arg
    command_line_check()

    #try to open file
    try:
       file=open(sys.argv[1],"r")
       lines=file.readlines()


    #pass error if cannot open
    except FileNotFoundError:
        sys.exit("file doesnt exist")
   #check it starts with # or whitespace
    count=0
    for line in lines:
        if check_lines(line)==False:
            count+=1
    print(count)


def command_line_check():
    #check how many element in it
    if len(sys.argv)>2:
        sys.exit("too many argument")
    if len(sys.argv)<2:
        sys.exit("too less argument")

    #python file or not
    if ".py" not in sys.argv[1]:
        sys.exit("NOT a python file")


def check_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__=="__main__":
    main()
