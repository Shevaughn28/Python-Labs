from datetime import datetime
heading= "HELLO WORLD LAB 1 - ACTIVITY 2"
a= heading.center(100)
print(a)
print("\n\nThis program will require the following information to be entered:")

name = input("Enter Name: ") #name input 
yob= input("Enter Year of Birth: ") #yob input
print("\n\nHello "+ name+"! Year of birth entered is "+yob)

currenty=datetime.now().year #obtaining the current year
age= currenty - int(yob)

#Using conditional operators to print results
if age>0:
    print("Your age must approximately "+ str(age) +" years")
elif age==0:
    print("Looks like you were born this year, hence your age is 0 Years!")
else:
    print("Entered Year Of Birth is greater than the current year. Please Re-Run the program.")
print("Goodbye, "+name+"!")