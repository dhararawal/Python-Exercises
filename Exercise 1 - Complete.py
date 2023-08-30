#import the date program from the datetime library
from datetime import date

#Ask the user to input their date of birth in the format DD/MM/YYYY
birthday = input("Enter your birthday as DD/MM/YYYY: ")

#Split user birthday and convert to int
birthDay = int(birthday.split("/", 1)[0]) #splits birth day
birthMonth = int(birthday.split("/", 2)[1]) #splits birth month
birthYear = int(birthday.split("/", 3)[2]) #splits birth year'''

#Assign today's date to the variable currentdate
currentdate = date.today()

#function to calculate the age of the user
def age():
    currentdate = date.today()
    age = currentdate.year - birthYear - ((currentdate.month, currentdate.day) < (birthMonth, birthDay))
    print("You are", age, "year(s) old!") #prints users age
age() #calls the function above

if currentdate.month == birthMonth and currentdate.day == birthDay:
    print("Happy Birthday!")
elif currentdate.month > birthMonth or currentdate.month == birthMonth and currentdate.day > birthDay:\
    print("Your birthday has passed!, Happy Belated Birthday!")
else:
    print("Your birthday is coming soon!")


