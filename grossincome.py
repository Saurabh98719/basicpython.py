# wap to calculate the gross income of a family

members = int(input("Enter number of family members: "))

if members <= 0:
    print("Number of family members must be positive.")
else:
    total_income = 0.0
    for i in range(1, members + 1):
        income = float(input(f"Enter income for member {i}: "))
        total_income += income

    print(f"Total gross income of the family: {total_income:.2f}")
