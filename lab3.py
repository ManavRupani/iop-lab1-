#      PENNY_VALUE = 1
#      NICKEL_VALUE = 5
#      DIME_VALUE = 10
#      QUARTER_VALUE = 25
#      PENNIES_IN_DOLLAR = 100

user_p = int(input("Enter the number of pennies: "))
user_n = int(input("Enter the number of nickels: "))
user_d = int(input("Enter the number of dimes: "))
user_q = int(input("Enter the number of quarters: "))

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

output = (user_p * PENNY_VALUE) + (user_n * NICKEL_VALUE) + \
              (user_d * DIME_VALUE) + (user_q * QUARTER_VALUE)

total_dollars = output / PENNIES_IN_DOLLAR
if total_dollars==1:
    print("Congratulations!\nThe amount you entered was exactly one dollar!\nYou win the game!!")
elif total_dollars < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
elif total_dollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
else:
    pass
