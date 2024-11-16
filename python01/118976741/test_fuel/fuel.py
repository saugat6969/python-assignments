


def main():

      fraction=str(input("Fraction: "))
      fraction_conv=convert(fraction)
      output=gauge(fraction_conv)
      print(output)


def convert(fraction):
    while True:

      try:
        x,y=fraction.split('/')
        numerator=int(x)
        denominator=int(y)
        decimal=numerator / denominator
        if decimal<=1:
            p=int(decimal*100)
            return p
        else:
            fraction=input("fraction")


      except (ValueError,ZeroDivisionError):
          raise






def gauge(percentage):
    if percentage<=1:
        return 'E'
    if percentage>=99:
        return 'F'
    else:
        return str(percentage)+'%'

    


if __name__ == "__main__":
    main()
