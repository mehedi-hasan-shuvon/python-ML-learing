#...............Tuples.............
#if we dont want to change the value of list we can use tuples insted of list

tup1=(1,2,4)
print(tup1)
print(tup1[0])
#tup1[0]=2   <............... we can not do that ,, this will give error cz tuples value can not be change
print(tup1)

#to change tuples value we have to conver it into the list first
#to make a tuple a list bellow code is needed
list1=list(tup1)
print(list1)
list1[0]=4
print(list1)
