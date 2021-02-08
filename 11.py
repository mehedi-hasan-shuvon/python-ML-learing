#.................File IO..........


#create a file with wb mode.........
file1=open("shuvon.txt","wb")
print(file1.mode)
print(file1.name)

#write inside the file
file1.write(bytes("write this to my file","UTF-8") )
file1.close() # if i dont close the file other program can not use that file...

