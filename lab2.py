

def takeInput(**arg):                           #taking input as arg muliple inputs 
    a=int(input("Enter a number "))
    b=int(input("Enter second number "))
    sign_=str(input("Select an operator (/,*,-,+) "))
    return [a,b,sign_]

def displayResult(ar,br,sign_r):        #processing and output as string
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

list_=takeInput()                   #calling function
a=list_[0]
b=list_[1]                          #unpacking values
c=list_[2]
output2=displayResult(a,b,c)        #calling function