def main():
    price=50
    total_paid=0
    print("Amount Due:",price)
    while total_paid<price:
        inserted_coin=int(input("insert coin: "))
        if inserted_coin==10 or inserted_coin==5 or inserted_coin==25:
            total_paid+=inserted_coin
            if total_paid <price:
                print("Amount Due:",price-total_paid)
        else:
          print("Amount Due:50")



    change=total_paid-price
    print("Change Owed:",change)

main()


