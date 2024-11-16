items={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=0

while True:
    try:
        choice=input("Items: ").title()

        if choice in items:
            total+=items[choice]
            print("total: $",end="")
            print("{:.2f}".format(total))
    except EOFError:
        print()
        break
    # except KeyboardInterrupt:
    #     print("\nOperation cancelled by user. Exiting.")

    #     break
