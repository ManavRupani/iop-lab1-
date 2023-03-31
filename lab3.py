#      PENNY_VALUE = 1
#      NICKEL_VALUE = 5
#      DIME_VALUE = 10
#      QUARTER_VALUE = 25
#      PENNIES_IN_DOLLAR = 100

num_pennies = int(input("Enter the number of pennies: "))
num_nickels = int(input("Enter the number of nickels: "))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

output = (num_pennies * PENNY_VALUE) + (num_nickels * NICKEL_VALUE) + \
              (num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE)

count = output / PENNIES_IN_DOLLAR

if count > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
elif count < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!\nThe amount you entered was exactly one dollar!\nYou win the game!!")
