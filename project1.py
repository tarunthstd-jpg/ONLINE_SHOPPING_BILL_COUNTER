print("Online Shopping Bill Counter")
print("Enter item prices")
print("Enter 0 to stop")
total = 0
count = 0
while True:
    price = int(input("Enter price: "))
    if price == 0:
        break
    if price < 0:
        print("Invalid price")
        continue
    total += price
    count += 1
    print("Item added")
print("------")
print("Items purchased:", count)
print("Total bill:", total)
tax = total * 0.05
print("Tax:", tax)
grand_total = total + tax
print("Grand total:", grand_total)
print("Payment successful")
print("Thank you")

