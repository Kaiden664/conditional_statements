actual_cost = float(input("Enter the actual product price: "))
selling_price = float(input("Please enter the selling price: "))
if (selling_price > actual_cost):
    print("total profit made:", selling_price - actual_cost)
else:
    print("no profit")