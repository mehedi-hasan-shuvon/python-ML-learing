#................lists...............

universities=['bracu','Du','buet']
#print a list
print(universities)
#print a specific index of a list
print(universities[0])

# chnage the value of a index in the list
universities[2]='kuet'
print(universities[2])
print(universities)
print(universities[1:3])

#adding a new element in the list
universities.append('nsu')
print(universities)

#insert into list
universities.insert(2,'nsu')
print(universities)
universities.remove('nsu')
print(universities)

print(universities+['ruet','aiub','eden'])
print(universities)
print(len(universities))
print(max(universities))# it sort dictionary wise
print(min(universities))# it sort dictionary wise

#list of list
list2=[[1,2,3],[4,5,6],[7,8,9]]    

for item in list2:
    for i in item:
        print(i)