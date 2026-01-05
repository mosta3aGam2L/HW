name=input("entre your name :")
age=int(int(input("entre the age :")))
height=float(input("entre the height :"))

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

sum=int(num1+num2)
deff=float(num1-num2)
product=num1*num2
div=float(num1/num2)

if num1 < 0 and num2 < 0:
            print("Both numbers are negative")
    
else:
            print("At least one number is positive")

print("\nOdd numbers from 1 to 19:")
for i in range(1, 20):
            if i % 2 != 0:
                print("Odd number:", i)

