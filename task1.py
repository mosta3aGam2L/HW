'''Q1'''
'''
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
//'''


'''Q2'''
'''
secret=7
guess=None
print(" Geuss two  nums")
while guess != secret:
            guess = int(input("Enter your guess: "))
            if guess != secret:
                print("Wrong guess, try again!")

print("Correct! You guessed the number.\n")

'''
'''Q3'''
'''
list=[1,2,3,4,5]
for i in list:
 #       print("sum =",i+1)
        print("sum =",sum(list))       
        print("max =",max(list))
#print("Reversed =",reversed(list))
#       print("REversd :",list[,-1])

 ################33
tuple=("cairo","alex","zagazig")
print("frist city",tuple[0]," || " ,"end",tuple[-1] )
'''
##############
 '''
group1 = {"Ali", "Sara", "Mona", "Omar"}
group2 = {"Mona", "Omar", "Ahmed"}

all_student=[]   #store 

for student in group1:
        if student in group2:
            all_student.append(student)
for student in all_student:
       print(" ",student)          
###################
'''
##################################
# not my effort#
#2 function to convert
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

#AVERAGE
def average_temperature(temp_list, scale='C'):
    avg = sum(temp_list) / len(temp_list)
    if scale.upper() == 'C':
        return avg
    else:
        return celsius_to_fahrenheit(avg)

def highest_temperature(temp_list, scale='C'):
    high = max(temp_list)
    if scale.upper() == 'C':
        return high
    else:
        return celsius_to_fahrenheit(high)
   
temps_input = input("Enter temperatures in Celsius (comma-separated): ")
list = []
for t in list_input.split(','):
            t = t.strip()  
            temps.append(float(t))

avg_c = average_temperature(list)
high_c = highest_temperature(list)

avg_f = celsius_to_fahrenheit(avg_c)
high_f = celsius_to_fahrenheit(high_c)

print("\nAverage Temperature:")
print("Celsius:", avg_c)
print("Fahrenheit:", avg_f)

print("\nHighest Temperature:")
print("Celsius:", high_c)
print("Fahrenheit:", high_f)
    
