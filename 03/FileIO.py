myFile = open('test.txt')
print(myFile.read())
print(myFile.read())
myFile.seek(0)
print(myFile.read())
myFile.seek(0)
contents = myFile.read()
print(contents)
myFile.seek(0)
contents = myFile.readlines()
print(contents)
myFile.seek(0)
contents = myFile.readline()
print(contents)
myFile.close()

with open('test.txt','w') as myNewFile:
    contents = myNewFile.write('Hi I wrote this text using Python!')
    print(contents)


with open('test.txt','r') as myNewFile:
    contents = myNewFile.read()
    print(contents)

with open('test.txt','a') as myNewFile:
    contents = myNewFile.write('Hi I wrote this text using Python!\n')
    print(contents)

with open('test.txt','r') as myNewFile:
    contents = myNewFile.readlines()
    print(contents)