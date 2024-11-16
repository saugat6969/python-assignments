#Expects zero or two command-line arguments:
import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
figlet.getFonts()

if len(sys.argv)==1:
   font=random.choice(figlet.getFonts())
  

elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font" ):

     font=sys.argv[2]
     if font in figlet.getFonts():
       figlet.setFont(font=font)

     else:
       print("invalid usage")
       sys.exit(1)

else:
   sys.exit(1)
msg=input("input: ")
print("output",f"{figlet.renderText(msg)}")

# import sys
# from pyfiglet import Figlet
# import random
# figlet = Figlet()
# figlet.getFonts()
# msg=input("input: ")

# if len(sys.argv)==1:
#    font=random.choice(figlet.getFonts())
#    print("output",f"{figlet.renderText(msg)}")

# elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font" ):
#    try:
#      figlet.setFont(font=sys.argv[2])
#      print("output",f"{figlet.renderText(msg)}")
#    except:
#      print("invalid")
#      sys.exit()

# else:
#    sys.exit(1)
