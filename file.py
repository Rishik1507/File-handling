file=open("sample.txt")
print(file.read())
file.close()

f=open("sample.txt","w")
f.write("Hello, \n")
f.write("I am Rishik")

a=open("sample.txt","a")
a.write("\n I am 14 years old..")

