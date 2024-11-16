answered=input(str("Greeting:"))
if "hello" in answered.lower().strip():
    print("$0")

elif "h"==answered.lower().strip()[0]:
    print("$20")
else:
    print("$100")
