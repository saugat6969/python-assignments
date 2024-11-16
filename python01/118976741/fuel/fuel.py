while True:
    x=str(input("Fraction: "))

    try:
        num,deno=x.split('/')
        numerator=int(num)
        denominator=int(deno)
        decimal=numerator / denominator
        percentage=int(decimal*100)

    except ValueError:
        print("not a correct value")
    except ZeroDivisionError:
        print("can't be zero(0) at denominator")

    else:
        break



if percentage<=1:
    print("E")
elif percentage>=99:
    print("F")
else:
    print(f"{percentage}%")
