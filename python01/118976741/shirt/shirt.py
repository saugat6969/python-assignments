import sys
from os.path import splitext
from PIL import Image,ImageOps
def main():
    command_line()
    #open image
    try:
        imagefile=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("input doesnt exist")
#open shirt


    shirt=Image.open('shirt.png')
#size
    size=shirt.size
    muppet= ImageOps.fit(imagefile,size)
    muppet.paste(shirt,shirt)
    muppet.save(sys.argv[2])



def command_line():
    if len(sys.argv)<3:
        sys.exit("too few argument")
    if len(sys.argv)>3:
        sys.exit("too many argument")
    if not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png") or sys.argv[1].endswith(".jpeg")):
        sys.exit("invalid input")
    if not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png") or sys.argv[2].endswith(".jpeg")):
        sys.exit("invalid output")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if (file1[1].lower())!=(file2[1].lower()):
        sys.exit("Input and output have different extensions")







if __name__=="__main__":
    main()
