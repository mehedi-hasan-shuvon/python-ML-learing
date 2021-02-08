#....... while loops..........

number=int(input("enter a number: "))

while number>4  :
    print("number is greater than 4")
    number =int(input())
    if number==9:
        break
    if number ==8:
        continue # continue means the the  code will go to the while loop again without cheching the rest
    print("loop ended ")