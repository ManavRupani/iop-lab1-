def takeInput(a,b,sign_):
    a=int(input("Enter a number "))
    b=input("Enter second number")
    sign_=input("Select an operator")
    return a,b,sign_

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