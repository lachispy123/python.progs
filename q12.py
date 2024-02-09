# take input of electricity unit charges
units = int(input("Enter the total number of units consumed: "))

# calculate the electricity bill according to the given conditions
if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 25 + (units - 50) * 0.75
elif units <= 250:
    bill = 100 + (units - 150) * 1.20
else:
    bill = 220 + (units - 250) * 1.50

# add 20% surcharge to the bill
total_bill = bill + bill * 0.20

# display the total electricity bill
print("Total electricity bill (including 20% surcharge) = Rs.", total_bill)
