f1=open("sample.txt")
f2=open("s.txt")
print("Content of file 1: ",f1.read())
print("Content of file 2:",f2.read())
f1.close()
f2.close()
f1=open("sample.txt")
f2=open("s.txt","a")
f2.write(f1.read())
f1.seek(0)
f2.seek(0)