h=float(input("Enter your height in meters: "))
w=float(input("Enter your Weight in Kg: "))
 
BMI=w/(h*h)
print("BMI Calculated is:  ",BMI)
 
if(BMI>0):
    if(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("Congrats! you are normal")
    else:
        print("You are overweight")
else:
    print("enter valid details")
