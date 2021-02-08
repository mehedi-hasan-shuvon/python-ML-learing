#........if else statements.........

number =int (input ("enter your marked: "))
print(number)

if number>=90 and number<=100:
    grade='A'
elif number>=80:
    grade='B'
else:
    grade='fail'


print("the grade is" ,grade)