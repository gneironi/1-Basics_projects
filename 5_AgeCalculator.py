#We use the today's date and the date of birth to calculate the Age.
import datetime


#creating a function to calculate the age
def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days / 365.25)
    print(f" Your age is: {age} years old")

#input the user data
y = int(input("Type your age of birth: "))
m = int(input("Type your month of birth: "))
d = int(input("Type your day of birth: "))

#run the function
ageCalculator(y, m, d)

