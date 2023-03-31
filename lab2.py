

def takeInput(**arg):
    a=int(input("Enter a number "))
    b=int(input("Enter second number "))
    sign_=str(input("Select an operator (/,*,-,+) "))
    return [a,b,sign_]

def displayResult(ar,br,sign_r):
    output=0
    if sign_r=="*":
        output=ar*br
    elif sign_r=="+":
        output=ar+br
    elif sign_r=="-":
        output=ar-br
    elif sign_r=="/":
        output=ar/br
    print(f"{ar} {sign_r} {br} = {output}")

list_=takeInput()
a=list_[0]
b=list_[1]
c=list_[2]
output2=displayResult(a,b,c)