print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVIDION")
option=int(input("choose an operation:"))
result=0
if(option in [1,2,3,4]):
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    if(option==1):
        result=num1+num2
    elif(option==2): 
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2
else:
    print("INVAILD OPERATIONAL CHOICE")
print("THE RESULT OF THE OPERATION IS:- {}".format(result))