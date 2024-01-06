#1 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount. 
employee_salary = int(input("Enter your salary"))
employee_service_years = int(input("Enter your service years"))

if employee_service_years > 5:  
    bonus = 5 * employee_salary
    net_bonus = (bonus + employee_salary )
    print("congratulations You are eligible for a bonus")
    print("your bonus amount is",bonus )
    print("your net bonus amount is",net_bonus )
else:
     print("Sorry you are not eligible for a bonus NEXT TIME.") 

#2 Write a program to check whether a person is eligible for voting or not. 
#(accept age from user) if age is greater than 17 eligible otherwise not eligible
    
person_age = int(input("Enter your age: "))

if person_age > 17:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  

 #3 Write a program to check whether a number entered by user is even or odd.

even_odd_num = int(input("Enter any number"))

if even_odd_num %2==0:
   print("This is even number")
else:
   print("This is odd number")    

#4 Write a program to check whether a number is divisible by 7 or not.
# Show Answer   

number = int(input("Enter any number"))
if number %7 == 0:
   print("it is divisible by 7")
else:
   print("is not divisible by 7")

#5 Write a program to display "Hello" if a number entered by user is a multiple of ve , 
#otherwise print "Bye"
   
number = int(input("Enter one digit number"))

if number %5 ==0:
   print("Hello")
else:
   print("Bye")

#6) Write a program to calculate the electricity bill (accept number of unit from user) 
#according to the following criteria :
#     Unit                                                     Price  
#uptp 100 units                                             no charge
#Next 200 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs.3500
#(For example if input unit is 97 than total bill amount is Rs.0
#(For example if input unit is 150 than total bill amount is Rs.750
   
Bill = float(input("Enter your electricity bill unit: "))
units200 = (Bill * 5)
units_AB_200 = (Bill * 10)

if Bill <=100:
    print("no charge free electricity ")
elif Bill >100 and Bill <200 :
    print("your electricity bill is ",units200,"Rs 5 per unit")
elif Bill >=200:
    print("your electricity bill is ",units_AB_200,"Rs 10 per unit")

#7) Write a program to display the last digit of a number.

Number = int(input("enter any number"))
last_digit = Number % 10

print("The last digit of", Number, "is:", last_digit)

#Q8. Write a program to check whether the last digit of a number
#( entered by user ) is divisible by 3 or not.

Num = int(input("Enter any number"))
last_digit = Num % 10

if last_digit%3==0:
    print("This", last_digit ,"number is divisible by 3")
else:
    print("This", last_digit , "number is not divisible by 3")

#9) Take values of length and breadth of a rectangle from user 
#   and print if it is square or rectangle.
    
lenght = float(input("Enter the lenght of rectangle:"))
breadth = float(input("Enter the breadth of rectangle:"))
if lenght ==breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")

#10) Take two int values from user and print greatest among them.
  
number1 = int(input("Enter any value"))
number2 = int(input("Enter any value"))

if number1 >= number2:
    print("this number1",number1,"is greatest")
elif number2 >= number1:
    print("this number2",number2,"is greatest")

#11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.
    
quantity = int(input("Enter quantity"))
unit = (quantity * 100)
discount = 0.10 * unit
total_cost = (unit - discount)

if unit >1000:
    total_cost = (unit - discount)
    print("your quantity is",unit,"And you get 10% discount:",total_cost)
else:
    print("your quantity is",unit,"And you get 0% discount:",unit)

#12) A school has following rules for grading system:
#a. Below 25 - 
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.
    
marks = float(input("Enter your marks"))

if marks <25:
    print("Your Grade is F")
elif marks >=25 and marks <45:
     print("Your Grade is E")
elif marks >=45 and marks <50:
      print("Your Grade is D")
elif marks >=50 and marks <60:
     print("Your Grade is C")
elif marks >=60 and marks <80:
     print("Your Grade is B")
elif marks >80:
     print("Your Grade is A")

#13) Take input of age of 3 people by user and determine oldest and youngest among them.         

person1 = int(input("Enter age of person 1: "))
person2 = int(input("Enter age of person 2: "))
person3 = int(input("Enter age of person 3: "))

if person1 >=person2 and person1 >=person3:
    print("Person1",person1,"is greatest")
elif person2 >=person1 and person2 >=person3:
     print("Person2",person2,"is greatest")
elif person3 >=person1 and person3 >=person2:
     print("Person3",person3,"is greatest")

#14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

Number_of_class_held = int(input("Enter Number of class held"))
Number_of_class_attended = int(input("Enter Number of class attended"))
percentage_of_class_attended = (Number_of_class_attended / Number_of_class_held)
pah = (percentage_of_class_attended * 100)

print(pah,"%")

if pah>=75:
   print("This student is allowed to sit in exam")
else:
   print("This student is not allowed to sit in exam")       

#15) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not 
#( 'Y' or 'N' ) and print accordingly.
   
medical = input("if you have medical cause or not Enter 'y' for yes 'n' for no: ")

if medical == "y":
    print("you are sit in medical cause")
else:
    print("you are not sit in medical cause")

#16) Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but if the year is century year 
#like 2000, 1900, 2100 then it must be divisible by 400.
    
year = int(input("Enter your fav year"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"it is leap year")
else:
    print(year,"it is not leap year")

#17) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"
    
age = int(input("Enter your age"))
gender = input("Enter your gender write 'M' or 'F'")
marital_status = input("Enter your marital status write 'Y' or 'N'")

if gender == "F":
    print("she will work only in urban areas")
elif gender == "M" and age >=20 and age <=40:
    print("he may work in anywhere")
elif gender == "M" and age >40 and age <=60:
    print("he will work in urban areas only")
elif age <20 and age >60:
    print("?")