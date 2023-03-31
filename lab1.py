
# a="_____________Output_________________"
# x=a.center(100)
# print(x)
count=0
tax=0
output=0
print(("Melanie Dental Clinic").center(100))
p_name=input(("Enter patient's name: "))
cl=input("Was cleaning performed? (y/n): ")
cv=input("Was cavity-filling performed? (y/n): ") 
x_ray=input("Was X-Ray performed? (y/n): ")
if cl=="y":
    count+=60
if cv=="y":
    count+=200
if x_ray=="y":
    count+=100

if count>300:
    count=count-count*(0.10)
elif count>200:
    count=count-count*(0.5)
else:
    pass
output=count*0.15
print("\n")
print("Melanie Dental Clinic")
print(("-"*100).center(100))
print("Receipt for patient name: ",p_name)
print("-"*100)
print(" Subtotal: ",count)
print("      Tax: ",output)
print("-"*100)
print("    total: ",count+output)

# print(output)