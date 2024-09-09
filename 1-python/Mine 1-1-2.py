check = float(input("Input the check amount: "))
tip = float(input("Input the tip %: "))
diners = int(input("Input the number of diners: "))
total = (check + check*(tip/100))
split = total/diners
print(f"Total Bill with Tip is ${total:.2f}")
print(f"Amongst the {diners} of you, the bill evenly split is ${split:.2f} per person")