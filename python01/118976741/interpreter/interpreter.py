expression=input("Expression: ")
x ,y, z =expression.split(" ")
new_x=float(x)
new_z=float(z)

if y=="+":
    output=new_x + new_z
if y=="-":
    output=new_x - new_z
if y=="*":
    output=new_x * new_z
if y=="/":
    output=new_x / new_z
print(round(output,1))
